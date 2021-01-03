/*----------------------------------------------------------------------------
| Project: CANapeAPI
|
| Description:
|
|   Start and Stop CANape with CANapeAPI.DLL
|
----------------------------------------------------------------------------*/

#include <windows.h>
#include <iostream>
using namespace std;

#include <typeinfo>
#include <stdio.h>
#include <conio.h>
#include <time.h>
#include <dos.h>
#include <limits.h>
#include <float.h>

#include "canapapi.h"
#include "AdditionalFunctions.h"

#if defined(_DEBUG) && defined(_AFXDLL)
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif
#define ASAP2_FILE "ASAP2_Demo_V161.a2l"
#define WORK_DIR "C:\\Users\\Public\\Documents\\Vector CANape 19.0\\ExampleDAQXCPSys"
#define MODULE_NAME "test_module"

#define MAX_TASK 10
#define MAX_CHNL 32

#define MAX_SAMPLE_SIZE 320
#define MAX_FIFO_SIZE   8000

typedef struct {
    unsigned short taskId;
    char channel[MAX_CHNL][64];
} VAcquisition;


int main(int argc, char** argv) {

#ifdef CALIBRATION
    FILE* fp;
    char Line[500];
#endif
    TAsap3Hdl Hdl = NULL;

    cout << "type_info(TAsap3Hdl): " << typeid(Hdl).name() << Hdl << endl;
    cout << "type_info(TAsap3Hdl): " << typeid(&Hdl).name() << &Hdl << endl;


    //  int i,n;
    //  bool Result = false;
    int t = 0, v;
    bool detachModule = false;
    char workDir[_MAX_PATH];




    char asap2[256];
    char name[256];
    char moduleName[256] = "Console";
    char* pArg;
    unsigned short chnl = 1;
    unsigned short task_Id;
    VAcquisition taskList[MAX_TASK];
    // set values of this structure, otherwise some value like 0xccccc
    // exist in debug version, this causes to reset data aqu. channels
    // before selecting a channel
    memset(&taskList, 0, sizeof(VAcquisition) * MAX_TASK);

    TModulHdl module = NULL;
    version_t dllVersion;
    short driverType = ASAP3_DRIVER_UNKNOWN;
    bool bModal = false;
    bool bDebug = true;
    bool bClearDeviceList = true;
    char* pErrMsg;   // If Error occurs, this is the error variable
    unsigned short errCode = 0;

    if (!Asap3GetVersion(&dllVersion) ||
        !(dllVersion.dllMainVersion == CANAPE_API_MAIN_VESION &&
            dllVersion.dllSubVersion == CANAPE_API_SUB_VESION &&
            dllVersion.dllRelease >= CANAPE_API_RELEASE)) {

        cout << "Wrong DLL-Version, some problems may occur." << endl;
    }

    cout << "CANapeAPI console------------------" << endl;
    cout << "Format: CONSOLE [-w <workdir>] [-a <asap2file>] [-c channel] [-v] [-h handle]" << endl;
    cout << "       -v   Make visible cancel button of CANape" << endl;
    cout << "       -c   channel = {1 | 2 | 3 | 4}: logical CAN channel number" << endl;
    cout << "       -h   module handle of existing client-server connection" << endl;
    cout << "       -t <driver_type>     <driver_type>={CCP|CAN|XCP_CAN|XCP_UDP|LIN|FLX|CANDELA|ETHERNET|SOME/IP|DLT}" << endl;
    cout << "       -m module_name" << endl;
    cout << "       -x   enable CANape menu" << endl;
    cout << "       -d-, -d+   disable/enable debug mode" << endl;

    memset(workDir, 0, sizeof(workDir));
    strcat(workDir, WORK_DIR);
    asap2[0] = 0;



    // if (strlen(argv[arg]) > 2) {
    //     sscanf(&argv[arg][2], "%d", (int*)&module);
    // }
    // else if (arg + 1 < argc) {
    //     arg++;
    //     sscanf(argv[arg], "%d", (int*)&module);
    // }
    // bClearDeviceList = false;
    // cout << "Modul Handle = " << module << endl;
    // cout << "ClearDeviceList disabled!" << endl;

    //strncpy(asap2, ASAP2_FILE, sizeof(asap2));
    //chnl = 2;
    //strncpy(moduleName, MODULE_NAME, sizeof(moduleName));

    //##### Driver Type
    // driverType = ASAP3_DRIVER_CCP;

    // driverType = ASAP3_DRIVER_CAN;

    // //"XCP_CAN"
    // driverType = ASAP3_DRIVER_XCP;
    // // chnl by default =1, can be set by -c <channel_nr>

    // //"XCP_UDP"
    // driverType = ASAP3_DRIVER_XCP;
    // chnl = 256;

    // driverType = ASAP3_DRIVER_LIN;
    // driverType = ASAP3_DRIVER_FLX;
    // driverType = ASAP3_DRIVER_CANDELA;
    // driverType = ASAP3_DRIVER_ETH;
    // driverType = ASAP3_DRIVER_SOME_IP;
    // driverType = ASAP3_DRIVER_DLT;



    //### Control CANape Menu
    bModal = true;

    bDebug = true;
    cout << "Debug mode " << ((bDebug) ? "enabled" : "disabled") << endl;



    cout << "Working directory is: \"" << workDir << "\"" << endl;
    if (asap2[0]) cout << "Selected ASAP2 is: \"" << asap2 << "\"" << endl;
    else          cout << "No ASAP2 selected" << endl;

    if (!Asap3Init5(&Hdl, 200000, workDir, MAX_FIFO_SIZE, MAX_SAMPLE_SIZE,
        bDebug/*debugMode*/, bClearDeviceList /*clearDeviceList*/,
        false/*bHexMode*/, bModal/*bModalMode*/)) {

        errCode = Asap3GetLastError(NULL);
        cout << "Asap3Init()-Fehler : " << errCode << endl;
        Asap3ErrorText(NULL, errCode, &pErrMsg);
        cout << "Result of Asap3ErrorText: " << pErrMsg << endl;

        if (errCode != AEC_FIFO_ALREADY_INIT)  return 0;
        cout << "The Fifo Memory Size was already initialized by another client" << endl;
    }

    cout << "Connection with CANape established..." << endl;
    cout << sizeof(Hdl) << " " << Hdl << " " << &Hdl << endl;

    //  Asap3PopupDebugWindow(Hdl);


    if (asap2[0]) {
        /*
            if (!Asap3CreateModule(Hdl, "test", asap2, ASAP3_DRIVER_CCP, chnl, &module)) {
              cout << "Asap3CreateModule()-Fehler" << endl;
              cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
            }
            else {
              cout << "Asap3CreateModule executed, module handle = " << module << endl;
              detachModule = true;
            }
        */

        if (driverType == ASAP3_DRIVER_UNKNOWN) {
            if (!Asap3CreateModule(Hdl, "TestDevice", asap2, ASAP3_DRIVER_CCP, chnl, &module)) {
                cout << "Asap3CreateModule()-Fehler" << endl;
                unsigned short errCodeVal = Asap3GetLastError(Hdl);
                cout << "Last error code = " << errCodeVal << endl;
                char* errMsg;
                Asap3ErrorText(Hdl, errCodeVal, &errMsg);
                cout << "Last error info = \"" << errMsg << "\"" << endl;
            }
            else {
                cout << "Asap3CreateModule executed, module handle = " << module << endl;
                detachModule = true;
            }
        }
        else {
            cout << "Asap3CreateModule(" << driverType << ")" << endl;

            if (!Asap3CreateModule(Hdl, moduleName, asap2, driverType, chnl, &module)) {
                cout << "Asap3CreateModule()-Fehler" << endl;
                unsigned short errCodeVal = Asap3GetLastError(Hdl);
                cout << "Last error code = " << errCodeVal << endl;
                char* errMsg;
                Asap3ErrorText(Hdl, errCodeVal, &errMsg);
                cout << "Last error info = \"" << errMsg << "\"" << endl;
            }
            else {
                cout << "Asap3CreateModule executed, module handle = " << module << endl;
                detachModule = true;
                UINT size = 0;
                Asap3GetDatabaseObjectsByType(Hdl, module, NULL, &size, DBTYPE_ALL, TDBE_VALUE_ALL);
                // Asap3GetDatabaseObjects(Hdl, module, NULL, &size, DBTYPE_ALL);
                char* Buffer = new char[size + 10];
                memset(Buffer, 0, size + 10);
                cout << "Asap3GetDatabaseObjects executed, module handle = " << module << endl;
                Asap3GetDatabaseObjectsByType(Hdl, module, Buffer, &size, DBTYPE_ALL, TDBE_VALUE_ALL);
                //        Asap3GetDatabaseObjects(Hdl, module, Buffer, &size, DBTYPE_ALL);
                DWORD counter = 0, oldpos = 0;
                DWORD x = 0;
                size = lstrlen(Buffer);

                while (counter < size)
                {
                    if (Buffer[counter] == ';')
                    {
                        char BufferOut[2 * _MAX_PATH];
                        memset(BufferOut, 0, sizeof(BufferOut));
                        memcpy(BufferOut, Buffer + oldpos, counter - oldpos);
                        printf("[%ld]%s\r\n", x, BufferOut);
                        oldpos = counter + 1;
                        x++;
                    }
                    counter++;
                }

                delete[] Buffer;

            }
        }
    }

    bool loop = true;
    int menu = 1;
    do {
        switch (menu) {
        case 1:
            cout << endl << "------------ Menu-1 ----------------------------" << endl;
            cout << "X:  exit" << endl << endl;
            cout << "A:  attach ASAP2" << endl;
            cout << "R:  read calibration object" << endl;
            cout << "W:  write calibration object" << endl;
#ifdef ADDRESS_FUNCTIONS
            cout << "J:  read by address" << endl;
            cout << "L:  write by address" << endl;
#endif
            cout << "Q:  select and read calibration object" << endl;
            cout << "T:  get ECU tasks (data acquisition)" << endl;
            cout << "I:  reset data acquisition" << endl;
            cout << "S:  select data acquisition channels" << endl;
            cout << "D:  start data acquisition via FIFO (press any key to stop)" << endl;
            cout << "Y:  start data acquisition, read current values (press any key to stop)" << endl;
            cout << "2:  ...more options" << endl;
            cout << "--------------------------------------------" << endl;
            break;
        case 2:
            cout << endl << "------------ Menu-2 ----------------------------" << endl;
            cout << "X:  exit" << endl << endl;
            cout << "H:  get module handle" << endl;
            cout << "C:  execute service" << endl;
            cout << "P:  execute script file (e.g. FaultMem.SCR)" << endl;
            cout << "E:  popup CANape write window" << endl;
            cout << "G:  read object parameter" << endl;
            cout << "K:  copy binary file" << endl;
            cout << "<:  get MDF file name" << endl;
            cout << ">:  set MDF file name" << endl;
            cout << "M:  convert MDF File to Matlab format" << endl;
            cout << "B:  test Asap3TransmitFile2ClientPc() of A2L to c:\\tmp\\tmp.a2l" << endl;
            cout << "1:  ...basic options menu" << endl;
            cout << "3:  ...diagnostic menu" << endl;
            cout << "--------------------------------------------" << endl;
            break;
        case 3:
            cout << endl << "---------- diagnostic menu -------------------" << endl;
            cout << "J:  Send Service 'Start Session'" << endl;
            //    cout << "U:  Send Service 'Stop  Session'" << endl;
            cout << "%:  Send Service 'ECU Identification - Read'" << endl;
            cout << "&:  Send Service 'ECU Serial_Number'" << endl;
            cout << "#:  Send Service 'Read Variant coding'" << endl;
            cout << "$:  Send Service 'Read DTC'" << endl;
            cout << "--------------------------------------------" << endl;
            cout << "/:  Set ODX Container'" << endl;
            cout << "(:  Get Session Count'" << endl;
            cout << "):  Get Session Name'" << endl;
            cout << "=:  Get Job Count'" << endl;
            cout << "?:  Get Job Name'" << endl;
            cout << "!:  Start Flash'" << endl;

            cout << "1:  ...basic options menu" << endl;
            cout << "2:  ...more options" << endl;
            cout << "--------------------------------------------" << endl;
            break;
        }
        int result = 0;

        int key = getch();
        switch (toupper(key)) {
        case 'B':
            if (asap2[0] == 0) {
                cout << "File transfer denied: no A2L file selected" << endl;
            }
            else
            {
                char buffer[_MAX_PATH];
                memset(buffer, 0, sizeof(buffer));
                GetTempPath(sizeof(buffer), buffer);
                _snprintf(buffer, sizeof(buffer), "%s%s", buffer, "tmp.a2l");
                if (Asap3TransmitFile2ClientPc(Hdl, asap2, buffer)) {
                    cout << "File transfer successful: " << asap2 << buffer << endl;
                }
                else {
                    cout << "File transfer failed: " << asap2 << buffer << endl;
                }
            }
            break;

        case 'X': loop = false; break;

        case '1': menu = 1; break;
        case '2': menu = 2; break;
        case '3': menu = 3; break;
        case 'G':
        {
            char nameStr[256];
            TAsap3DataType type;
            unsigned long address;
            double min, max, increment;

            cout << "Get Parameter Info\nInsert Name :";
            cout.flush();
            cin >> nameStr;

            cout << "Format ( 1 = ECU_INTERNAL | other key = PHYSICAL_REPRESENTATION):";
            cout.flush();
            int c = getch();
            TFormat format = PHYSICAL_REPRESENTATION;
            if (c == '1') format = ECU_INTERNAL;

            if (Asap3ReadObjectParameter(Hdl, module, nameStr, format, &type, &address, &min, &max, &increment)) {
                cout << "\nInfo Object: " << nameStr << "\nType\t: " << type << endl;
                printf("Address\t: %0xd", address);
                cout << "\nMin\t: " << min << "\nMax\t: " << max << "\nIncrement\t: " << increment << endl;
            }
            else {
                cout << "Error get parameter info" << endl;
                cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
                char* errMsg;
                Asap3ErrorText(Hdl, Asap3GetLastError(Hdl), &errMsg);
                cout << "Last error info = \"" << errMsg << "\"" << endl;
            }
            break;
        }
        case 'K':
        {
            char c, filename[256];
            TAsap3FileType st, dest;
            cout << "Copy Binary File \nEnter Source type (1 = FILE | 2 = VIRTUAL | 3 = PHYSICAL):";
            cout.flush();
            c = getch();
            switch (c) {
            case '1':
                st = TYPE_FILE;
                break;
            case '2':
                st = TYPE_VIRTUAL;
                break;
            default:
                st = TYPE_PHYSICAL;
                break;
            }

            cout << "\n\nEnter Destination type (1 = FILE | 2 = VIRTUAL | 3 = PHYSICAL):";
            cout.flush();
            c = getch();
            switch (c) {
            case '1':
                dest = TYPE_FILE;
                break;
            case '2':
                dest = TYPE_VIRTUAL;
                break;
            default:
                dest = TYPE_PHYSICAL;
                break;
            }
            if (dest == TYPE_FILE || st == TYPE_FILE) {
                cout << "\nEnter Filename:";
                cout.flush();
                cin >> filename;
            }
            else {
                strncpy(filename, "no filename required", 256);
            }

            if (Asap3CopyBinaryFile(Hdl, module, st, dest, filename)) {
                cout << "Copy binary file was successfully";
            }
            else {
                cout << "Error occurred: Copy binary file." << endl;
                char* errMsg;
                Asap3ErrorText(Hdl, Asap3GetLastError(Hdl), &errMsg);
                cout << "Last error info = \"" << errMsg << "\"" << endl;
            }
        }
        case '<':
        {
            char* filename;
            if (Asap3GetMdfFilename(Hdl, &filename)) {
                cout << "MDF file name: " << filename << endl;
            }
            else {
                cout << "Error occurred: Get MDF file name." << endl;
                char* errMsg;
                Asap3ErrorText(Hdl, Asap3GetLastError(Hdl), &errMsg);
                cout << "Last error info = \"" << errMsg << "\"" << endl;
            }
            break;
        }

        case '>':
        {
            char filename[256];

            cout << "\nEnter new Filename:";
            cout.flush();
            cin >> filename;

            if (Asap3SetMdfFilename(Hdl, filename)) {
                cout << "MDF file name set: " << filename << endl;
            }
            else {
                cout << "Error occurred: Set MDF file name." << endl;
                char* errMsg;
                Asap3ErrorText(Hdl, Asap3GetLastError(Hdl), &errMsg);
                cout << "Last error info = \"" << errMsg << "\"" << endl;
            }
            break;
        }

        case 'M':
        {
            char infile[256], outfile[256];

            cout << "\nEnter input MDF file:";
            cout.flush();
            cin >> infile;
            cout << "\nEnter output Matlab file:";
            cout.flush();
            cin >> outfile;


            if (Asap3MatlabConversion(Hdl, infile, outfile)) {
                cout << "Converted " << infile << "  to  " << outfile << endl;
            }
            else {
                cout << "Error occurred: Convert MDF file to Matlab file." << endl;
                char* errMsg;
                Asap3ErrorText(Hdl, Asap3GetLastError(Hdl), &errMsg);
                cout << "Last error info = \"" << errMsg << "\"" << endl;
            }
            break;
        }

        case 'E':
            cout << "Call Asap3PopupDebugWindow()";
            Asap3PopupDebugWindow(Hdl);
            break;
        case 'P':
            cout << "Insert script file name:  ";
            cout.flush();

            if (fgets(name, sizeof(name), stdin)) {
                if (name[strlen(name) - 1] == '\n') name[strlen(name) - 1] = 0;

                if (stricmp(name, "faultmem.scr") == 0) {
                    unlink("faultmem.txt");
                }
                if (!Asap3ExecuteScript(Hdl, module, true, name)) {
                    cout << "Asap3ExecuteScript()-Fehler" << endl;
                    cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
                }
                else {
                    cout << "Asap3ExecuteScript() durchgeführt" << endl;
                    if (stricmp(name, "faultmem.scr") == 0) {
                        // Datei anzeigen
                        char line[1024];
                        FILE* fp = fopen("faultmem.txt", "rt");
                        if (fp) {
                            while (fgets(line, sizeof(line), fp)) {
                                cout << line;
                            }
                            fclose(fp);
                        }
                    }
                }
            }
            break;

        case 'C':
            cout << "Insert request (hex):  ";
            cout.flush();
            if (fgets(name, sizeof(name), stdin)) {
                int index = 0;
                char* ptr = name;
                unsigned char cmd[256], res[256];
                unsigned long resLen;

                while (isspace(*ptr)) ptr++;

                while (*ptr != 0) {
                    cmd[index++] = (unsigned char)strtoul(ptr, &ptr, 16);
                    while (isspace(*ptr)) ptr++;
                }

                if (index > 0) {
                    cout << "Service: ";
                    for (int i = 0; i < index; i++) {
                        char buf[10];
                        sprintf(buf, "%02X ", cmd[i]);
                        cout << buf;
                    }
                    cout << endl;
                    if (!Asap3_CCP_Request(Hdl, module,
                        cmd, index, 1000, res, 255, &resLen)) {
                        cout << "Asap3_CCP_Request()-Fehler" << endl;
                        cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
                    }
                    else {
                        cout << "Response: ";
                        for (unsigned int i = 0; i < resLen; i++) {
                            char buf[10];
                            sprintf(buf, "%02X ", res[i]);
                            cout << buf;
                        }
                        cout << endl;
                    }
                }
            }

            break;

        case 'H':
            cout << "Insert module name:  ";
            cout.flush();
            if (fgets(asap2, sizeof(asap2), stdin)) {
                if (asap2[strlen(asap2) - 1] == '\n') asap2[strlen(asap2) - 1] = 0;

                if (!Asap3GetModuleHandle(Hdl, asap2, &module)) {
                    cout << "Asap3GetModuleHandle()-Fehler" << endl;
                    cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
                }
                else {
                    cout << "Asap3GetModuleHandle executed" << endl;
                }
            }
            break;
        case 'A':
            cout << "A:     AttachAsap2" << endl;
            if (detachModule) {
                detachModule = false;
                if (!Asap3ReleaseModule(Hdl, module)) {
                    cout << "Asap3ReleaseModule()-Fehler" << endl;
                    cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
                }
                else {
                    cout << "Asap3ReleaseModule():" << endl;
                }
            }
            cout << "Insert ASAP2 filename:  ";
            cout.flush();
            if (fgets(asap2, sizeof(asap2), stdin)) {
                if (asap2[strlen(asap2) - 1] == '\n') asap2[strlen(asap2) - 1] = 0;

                if (!Asap3AttachAsap2(Hdl, asap2, chnl, &module)) {
                    cout << "AttachAsap2()-Fehler" << endl;
                    unsigned short errCodeVal = Asap3GetLastError(Hdl);
                    cout << "Last error code = " << errCodeVal << endl;
                    char* errMsg;
                    Asap3ErrorText(Hdl, errCodeVal, &errMsg);
                    cout << "Last error info = \"" << errMsg << "\"" << endl;
                }
                else {
                    cout << "AttachAsap2 executed" << endl;
                    detachModule = true;
                }
            }
            break;
        case 'R':
            cout << "Insert Calibration object name:  ";
            cout.flush();
            if (fgets(name, sizeof(name), stdin)) {
                if (name[strlen(name) - 1] == '\n') name[strlen(name) - 1] = 0;

                ReadCalValue(Hdl, module, name, NULL /* double *newval */);
            }
            break;
        case 'W':
            cout << "Insert Calibration object name:  ";
            cout.flush();
            if (fgets(name, sizeof(name), stdin)) {
                if (name[strlen(name) - 1] == '\n') name[strlen(name) - 1] = 0;

                cout << "Insert Calibration object value:  ";
                cout.flush();
                char tmp[100];
                if (fgets(tmp, sizeof(tmp), stdin)) {
                    ReadCalValue(Hdl, module, name, tmp);
                }
            }
            break;
#ifdef ADDRESS_FUNCTIONS
        case 'J':
            cout << "Insert Address (hex):  ";
            cout.flush();
            if (fgets(name, sizeof(name), stdin)) {
                if (name[strlen(name) - 1] == '\n') name[strlen(name) - 1] = 0;
                unsigned long addr = strtoul(name, 0, 16);
                ReadAddrValue(Hdl, module, addr, NULL /* double *newval */);
            }
            break;
        case 'L':
            cout << "Insert Address:  ";
            cout.flush();
            unsigned long addr;
            if (fgets(name, sizeof(name), stdin)) {
                if (name[strlen(name) - 1] == '\n') name[strlen(name) - 1] = 0;
                addr = strtoul(name, 0, 16);
                cout << "Insert new Value (hex):";
                cout.flush();

                if (fgets(name, sizeof(name), stdin)) {
                    if (name[strlen(name) - 1] == '\n') name[strlen(name) - 1] = 0;
                    unsigned char value = strtoul(name, 0, 16);
                    //printf("Adress: 0x%x\t Value : 0x%X\n", addr, value);
                    ReadAddrValue(Hdl, module, addr, &value);
                }
            }
            break;
#endif

        case 'Q':
        {
            std::string w = workDir;
            w += "\\tmp.lst";
            if (!Asap3SelectObjects(Hdl, module, OTT_CALIBRATE, (char*)w.c_str())) {
                cout << "SelectAsap2Objects()-Fehler" << endl;
                cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
            }
            else {

                cout << "SelectAsap2Objects executed" << endl;
                FILE* fp = fopen((char*)w.c_str(), "rt");
                name[0] = 0;
                if (fp) {
                    while (fgets(name, sizeof(name), fp)) {
                        if (name[strlen(name) - 1] == '\n') name[strlen(name) - 1] = 0;

                        ReadCalValue(Hdl, module, name, NULL);
                    }
                    fclose(fp);
                }
            }
        }
        break;
        case 'T':
#define MAX_TASK_INFO 10
            TTaskInfo taskInfo[MAX_TASK_INFO];
            unsigned short noTasks;
            if (!Asap3GetEcuTasks(Hdl, module, taskInfo, &noTasks, MAX_TASK_INFO)) {
                cout << "Asap3GetEcuTasks()-Fehler" << endl;
                cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
            }
            else {
                cout << "Asap3GetEcuTasks() executed" << endl;
                cout << "noTasks=" << noTasks << endl;
                for (int i = 0; i < noTasks; i++) {
                    cout << "Task " << i << ": Id=" << taskInfo[i].taskId << " Description=" << taskInfo[i].description << endl;
                }
            }
            break;
        case 'I': // reset data acquisition
            for (t = 0; t < MAX_TASK; t++) taskList[t].taskId = 0;
            break;
        case 'S': // select data acquisition channels
            cout << "Select 'task id': ";
            cout.flush();
            if (fgets(name, sizeof(name), stdin) && strlen(name) > 0) {
                task_Id = (unsigned short)atoi(name);
                for (t = 0; t < MAX_TASK; t++) {
                    if (taskList[t].taskId == 0) {
                        break;
                    }
                    else if (taskList[t].taskId == task_Id) {
                        cout << "'Task Id' denied, because already used" << endl;
                        break;
                    }
                }
                if (t < MAX_TASK && taskList[t].taskId != task_Id) {
                    char fname[_MAX_PATH];
                    memset(fname, 0, sizeof(fname));
                    GetTempPath(_MAX_PATH, fname);
                    strcat(fname, "tmp.lst");
                    if (!Asap3SelectObjects(Hdl, module, OTT_MEASURE, fname)) {
                        cout << "SelectAsap2Objects()-Fehler" << endl;
                        cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
                    }
                    else {

                        taskList[t].taskId = task_Id;
                        taskList[t].channel[0][0] = 0;

                        cout << "SelectAsap2Objects executed" << endl;
                    }
                    if (fname) {
                        int index = 0;
                        FILE* fp = fopen(fname, "rt");
                        name[0] = 0;
                        if (fp) {

                            while (fgets(name, sizeof(name), fp)) {
                                if (name[strlen(name) - 1] == '\n') name[strlen(name) - 1] = 0;

                                if (index < MAX_CHNL) {
                                    strncpy(taskList[t].channel[index], name, sizeof(taskList[t].channel[index]));
                                }
                                if (++index < MAX_CHNL) {
                                    taskList[t].channel[index][0] = 0;  // Endekennung
                                }
                            }
                            fclose(fp);
                        }
                        else {
                            cout << "Can't open file " << fname << endl;
                        }
                    }
                }
            }
            break;
        case 'J':
        {
            cout << "ExecuteService EcuIdentification" << endl;
            TAsap3DiagHdl hDiag = DiagnosticCreate(Hdl, module, (char*)"EcuIdentification_Read");
            unsigned int ReponseCount = DiagnosticExecute(Hdl, hDiag);
            for (unsigned int i = 0; i < ReponseCount; i++) {
                DiagnosticStringGetParameter(Hdl, hDiag, i, (char*)"Ident_Number_Digit_7_6");
                DiagnosticStringGetParameter(Hdl, hDiag, i, (char*)"Ident_Number_Digit_5_4");
                DiagnosticStringGetParameter(Hdl, hDiag, i, (char*)"Ident_Number_Digit_3_2");
                DiagnosticStringGetParameter(Hdl, hDiag, i, (char*)"Ident_Number_Digit_1_0");
                DiagnosticStringGetParameter(Hdl, hDiag, i, (char*)"Diagnostic_Identification_dump");
            }
            DiagnosticRemoveService(Hdl, hDiag);
        }
        break;
        /*  case 'U':
            {
               cout << "ExecuteService Stop Session" << endl;
               TAsap3DiagHdl hDiag=DiagnosticCreate(Hdl,module,"STOP_SESSION/STOP_SESSION/Stop");
               unsigned int ReponseCount=DiagnosticExecute(Hdl,hDiag);
               for(unsigned int i=0;i<ReponseCount;i++){
                 DiagnosticGetRawStream(Hdl,hDiag,i);
               }
               DiagnosticRemoveService(Hdl,hDiag);
            }
          break;*/
        case '%':
        {
            cout << "ExecuteService SerialNumber - Read" << endl;
            TAsap3DiagHdl hDiag = DiagnosticCreate(Hdl, module, (char*)"SerialNumber_Read");
            unsigned int ReponseCount = DiagnosticExecute(Hdl, hDiag);
            for (unsigned int i = 0; i < ReponseCount; i++) {
                DiagnosticGetRawStream(Hdl, hDiag, i);
            }
            DiagnosticRemoveService(Hdl, hDiag);
        }
        break;
        case '#':
        {
            cout << "ExecuteService Read Variantcoding" << endl;
            TAsap3DiagHdl hDiag = DiagnosticCreate(Hdl, module, (char*)"Coding_Read");
            unsigned int ReponseCount = DiagnosticExecute(Hdl, hDiag);
            for (unsigned int i = 0; i < ReponseCount; i++) {
                DiagnosticStringGetParameter(Hdl, hDiag, i, (char*)"CodingString.StateVariant");
                DiagnosticStringGetParameter(Hdl, hDiag, i, (char*)"CodingString.VehicleType");
                DiagnosticStringGetParameter(Hdl, hDiag, i, (char*)"CodingString.SpecialPreference");
            }
            DiagnosticRemoveService(Hdl, hDiag);
        }
        break;
        case '&':
        {
            cout << "ExecuteService ECU Serial_Number" << endl;
            TAsap3DiagHdl hDiag = DiagnosticCreate(Hdl, module, (char*)"SerialNumber_Read");
            unsigned int ReponseCount = DiagnosticExecute(Hdl, hDiag);
            for (unsigned int i = 0; i < ReponseCount; i++) {
                DiagnosticGetRawStream(Hdl, hDiag, i);
            }
            DiagnosticStringGetParameter(Hdl, hDiag, 0, (char*)"SerialNumber");
            DiagnosticRemoveService(Hdl, hDiag);
        }
        break;
        case '$':
        {
            cout << "ExecuteService Read DTC" << endl;
            TAsap3DiagHdl hDiag = DiagnosticCreate(Hdl, module, (char*)"FaultMemory_ReadAllIdentified");
            DiagnosticSetParameter(Hdl, hDiag, (char*)"GroupOfDtc", (char*)"Powertrain group");
            int ReponseCount = DiagnosticExecute(Hdl, hDiag);
            BOOL IsComplex;
            if (Asap3DiagIsComplexResponseParameter(Hdl, hDiag, (char*)"ListOfDtcAndStatus", 0, &IsComplex))
                cout << "Complex parameter detected" << endl;
            unsigned long iteration = 0;
            Asap3DiagGetComplexIterationCount(Hdl, hDiag, (char*)"ListOfDtcAndStatus", 0, &iteration);

            for (int z = 0; z < ReponseCount; z++) {
                for (unsigned int i = 0; i < iteration; i++) {
                    cout << " Iteration " << i << endl;
                    DiagnosticStringGetComplexParameter(Hdl, hDiag, z, (char*)"ListOfDtcAndStatus", (char*)"DTC", i);
                    DiagnosticStringGetComplexParameter(Hdl, hDiag, z, (char*)"ListOfDtcAndStatus", (char*)"DtcStatus.DTCFaultSymptom", i);
                    DiagnosticStringGetComplexParameter(Hdl, hDiag, z, (char*)"ListOfDtcAndStatus", (char*)"DtcStatus.DTCReadinessFlag", i);
                    DiagnosticStringGetComplexParameter(Hdl, hDiag, z, (char*)"ListOfDtcAndStatus", (char*)"DtcStatus.DTCStorageState", i);
                    DiagnosticStringGetComplexParameter(Hdl, hDiag, z, (char*)"ListOfDtcAndStatus", (char*)"DtcStatus.DTCWarningLampCalibrationStatus", i);
                }
            }
            DiagnosticRemoveService(Hdl, hDiag);
        }
        break;

        case '/':
        {
            cout << "Insert ODX Flash container filename:  ";
            cout.flush();
            char OBXFile[MAX_PATH];
            if (fgets(OBXFile, sizeof(OBXFile), stdin)) {
                if (OBXFile[strlen(OBXFile) - 1] == '\n') OBXFile[strlen(OBXFile) - 1] = 0;

                Asap3FlashSetODXContainer(Hdl, module, OBXFile);
            }
        }
        break;
        case '(':
        {
            unsigned long Count = 0;
            if (Asap3FlashGetSessionCount(Hdl, module, &Count))
            {
                printf("\r\n %ld Sessions found", Count);
            }
        }
        break;
        case ')':
        {
            cout << "Insert a session index number:  ";
            cout.flush();
            unsigned long index;
            scanf("%ld", &index);
            char Session[MAX_PATH];
            long size = sizeof(Session);
            if (Asap3FlashGetSessionName(Hdl, module, index, Session, &size))
            {
                printf("\r\n %s Sessions found", Session);
            }
        }
        break;
        case '=':
        {
            unsigned long Count = 0;
            Asap3FlashGetJobCount(Hdl, module, &Count);
            printf("\r\n %ld Jobs found", Count);
        }
        break;
        case '?':
        {
            cout << "Insert a job index number:  ";
            cout.flush();
            unsigned long index;
            scanf("%ld", &index);
            char Job[MAX_PATH];
            long size = sizeof(Job);
            Asap3FlashGetJobName(Hdl, module, index, Job, &size);
            printf("\r\n Joc: %s ", Job);
        }
        break;

        case '!':
        {
            char Job[MAX_PATH];
            char Session[MAX_PATH];
            /*cout << "Insert a job name:  ";
            cout.flush();
            if (fgets(Job, sizeof(Job), stdin)) {
             cout << "Insert a session name:  ";
             cout.flush();
             if (fgets(Session, sizeof(Session), stdin)) {*/

            memset(Job, 0, sizeof(Job));
            long size = sizeof(Job);
            Asap3FlashGetJobName(Hdl, module, 0, Job, &size);

            memset(Session, 0, sizeof(Session));
            size = sizeof(Session);
            Asap3FlashGetSessionName(Hdl, module, 0, Session, &size);

            Asap3FlashStartFlashJob(Hdl, module, Session, Job, NULL);
            /*  }
             }*/
        }
        break;
        /*cout << "(:  Get Session Count'" << endl;
        cout << "):  Get Session Name'" << endl;
        cout << "=:  Get Job Count'" << endl;
        cout << "?:  Get Job Name'" << endl;
        cout << "!:  Start Flash'" << endl;*/

        case 'D': // start/stop data acquisition
      // sometime an overrun occurs because the console output
      // is to slow. Now, if an overun occure the count of
      // console output will be reduced and the overrun will not occur
        case 'Y':
            unsigned int overrunvalue = 0;  // value increas to overrunmax
            unsigned int overrunmax = 0;    // value output cycle
            bool getCurValues = (toupper(key) == 'Y') ? true : false;
            // double clockFact = 1.0;
            unsigned int delay = CLK_TCK;

            // Fifo lesen
            if (!Asap3ResetDataAcquisitionChnls(Hdl)) {
                cout << "Asap3ResetDataAcquisitionChnls()-Fehler" << endl;
            }
            else {
                cout << "Asap3ResetDataAcquisitionChnls():" << endl;

                for (t = 0; t < MAX_TASK; t++) {
                    if (taskList[t].taskId == 0) break;
                    for (v = 0; v < MAX_CHNL; v++) {
                        if (taskList[t].channel[v][0] == 0) break;
                        if (!Asap3SetupDataAcquisitionChnl(Hdl, module,
                            taskList[t].channel[v],
                            PHYSICAL_REPRESENTATION,
                            taskList[t].taskId, 250, false)) {
                            cout << "Asap3SetupDataAcquisitionChnl()-Fehler" << endl;
                            cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
                        }
                        else {
                            cout << "Setup: " << taskList[t].taskId << " - " << taskList[t].channel[v] << endl;
                        }
                    }
                }
                cout << "Asap3SetupDataAcquisitionChnl():" << endl;

                if (!Asap3StartDataAcquisition(Hdl)) {
                    cout << "Asap3StartDataAcquisition()-Fehler" << endl;
                    cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
                }
                else {
                    cout << "Asap3StartDataAcquisition():" << endl;

                    cout << "Press any key to stop data acquisition" << endl;
                    if (getCurValues) {
                        cout << "Press '+' or '-' to change display rate" << endl;
                    }

                    unsigned int _clock = clock();
                    for (;;) {
                        for (t = 0; t < MAX_TASK; t++) {
                            if (taskList[t].taskId == 0) break;

                            if (!getCurValues) {
                                if (Asap3CheckOverrun(Hdl, module, taskList[t].taskId, true)) {
                                    cout << "Overrun detected!" << endl;
                                    if (overrunmax < UINT_MAX) overrunmax++;
                                }
                                if (Asap3GetFifoLevel(Hdl, module, taskList[t].taskId) == 0) continue;
                            }


                            TTime timeStamp;
                            double* values, buffer[MAX_SAMPLE_SIZE];
                            bool rc;

                            if (getCurValues) {
                                // nur einen pro Sekunde
                                if (clock() > (clock_t)(_clock + delay)) {
                                    values = buffer;
                                    rc = Asap3GetCurrentValues(Hdl, module, taskList[t].taskId, &timeStamp, values, MAX_SAMPLE_SIZE);
                                    if (rc) {
                                        _clock = clock();
                                    }
                                }
                                else continue;
                            }
                            else {
                                rc = Asap3GetNextSample(Hdl, module, taskList[t].taskId, &timeStamp, &values);
                                /*                  tSampleBlockObject * values;
                                                  long  index=-1;
                                                  rc = Asap3GetNextSampleBlock(Hdl, module, taskList[t].taskId,index,&values);

                                                  for(int i=0;i<values->countofValidEntries;i++)
                                                  {
                                                    printf("\r\n[%ld]",values->tSample[i]->timestamp);
                                                  }
                                                  Sleep(300);
                                                  continue;*/
                            }

                            if (!rc) {
                                switch (Asap3GetLastError(Hdl)) {
                                case AEC_NO_VALUES_SAMPLED:
                                    break;
                                case AEC_ACQ_CHNL_OVERRUN:
                                    cout << "Asap3GetNextSample()-Fehler: channel overrun" << endl;
                                    break;
                                default:
                                    cout << "Asap3GetNextSample()-Fehler" << endl;
                                }
                            }
                            else {
                                if (overrunvalue >= overrunmax) {
                                    if (getCurValues) {
                                        cout << "Asap3GetCurrentValues(" << 1000.0 / delay << " Hz)" << endl;
                                    }
                                    else {
                                        cout << "Asap3GetNextSample()" << endl;
                                    }
                                    cout << "time = " << timeStamp << "  module = " << module << "  task = " << taskList[t].taskId << "  Werte = ";
                                    for (v = 0; taskList[t].channel[v][0]; v++) {
                                        _isnan(values[v]) ? cout << "?_" << v + 1 << "_?" << "   " : cout << values[v] << "  ";
                                    }
                                    cout << endl;
                                    overrunvalue = 0;
                                }
                                else overrunvalue++;
                            }
                        }

                        if (kbhit()) {
                            int keyVal = getch();
                            if (keyVal == '-')      delay = Quantisieren(true, delay);
                            else if (keyVal == '+') delay = Quantisieren(false, delay);
                            else                 break;
                        }

#if 0
                        if (clock() > _clock + 6 * CLK_TCK) {
                            _clock = clock();

                            if (!Asap3StopDataAcquisition(Hdl)) {
                                cout << "Asap3StopDataAcquisition()-Fehler" << endl;
                                cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
                                break;
                            }
                            if (!Asap3StartDataAcquisition(Hdl)) {
                                cout << "Asap3StartDataAcquisition()-Fehler" << endl;
                                cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
                                break;
                            }
                        }
#endif
                    }
                    if (!Asap3StopDataAcquisition(Hdl)) {
                        cout << "Asap3StopDataAcquisition()-Fehler" << endl;
                        cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
                    }
                    else {
                        cout << "Asap3StopDataAcquisition():" << endl;
                    }
                }
            }

            break;
        }
    } while (loop);

    if (detachModule) {
        if (!Asap3ReleaseModule(Hdl, module)) {
            cout << "Asap3ReleaseModule()-Fehler" << endl;
        }
        cout << "Asap3ReleaseModule():" << endl;
    }
    cout << "Exiting Hdl: " << Hdl << " " << &Hdl << endl;
    Asap3Exit(Hdl);
    cout << "CANapeAPI console terminated" << endl;
    return 0;
}
