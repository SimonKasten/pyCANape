#pragma once

#include <windows.h>
#include <iostream>
using namespace std;

#include <stdio.h>
#include <conio.h>
#include <time.h>
#include <dos.h>
#include <limits.h>
#include <float.h>

#include "canapapi.h"


long CALLBACK fnDiagNotification(unsigned long sizeofstruct, DiagNotificationStruct* str)
{
    SetEvent(str->PrivateData);
    return 0;
}

TAsap3DiagHdl DiagnosticCreate(TAsap3Hdl hdl, TModulHdl module, char* Request)
{
    TAsap3DiagHdl hDiag = 0;
    if (!Request) {
        cout << "Unknown Service name" << Request << endl;
        return 0;
    }

    //  FNCDIAGNOFIFICATION a;
    cout << "Service = " << Request << endl;
    if (!Asap3DiagCreateSymbolicRequest(hdl, module, Request, &hDiag)) {
        cout << "Asap3DiagCreateSymbolicRequest()-Error" << endl;
        cout << "Last error = " << Asap3GetLastError(hdl) << endl;
        return 0;
    }
    return hDiag;
}

bool DiagnosticSetParameter(TAsap3Hdl hdl, TAsap3DiagHdl Handle, char* Parameter, char* Value)
{
    if (Handle == 0)
        return false;

    if (!Asap3DiagSetStringParameter(hdl, Handle, Parameter, Value)) {
        cout << "Asap3DiagSetStringParameter()-Error" << endl;
        cout << "Last error = " << Asap3GetLastError(hdl) << endl;
        return false;
    }
    return true;
}

bool DiagnosticStringGetParameter(TAsap3Hdl hdl, TAsap3DiagHdl Handle, unsigned long ResponseID, char* ParameterName)
{
    if (Handle == 0)
        return false;

    DWORD Size = 0;
    char* Value = 0;

    // Call this function first with Value=NULL to get the necessary size of the char array
    if (!Asap3DiagGetStringResponseParameter(hdl, Handle, ParameterName, ResponseID, Value, &Size)) {
        cout << "Asap3DiagGetStringResponseParameter()-Error" << endl;
        cout << "Last error = " << Asap3GetLastError(hdl) << endl;
        return false;
    }

    if (Size == 0)
        return false;

    Value = new char[Size + 1];
    memset(Value, 0, Size + 1);

    // Now receive the parameter data

    if (!Asap3DiagGetStringResponseParameter(hdl, Handle, ParameterName, ResponseID, Value, &Size)) {
        cout << "Asap3DiagGetStringResponseParameter()-Error" << endl;
        cout << "Last error = " << Asap3GetLastError(hdl) << endl;
        delete[]Value;
        return false;
    }

    cout << ParameterName << ": " << Value << endl;
    delete[]Value;
    return true;
}

bool DiagnosticStringGetComplexParameter(TAsap3Hdl hdl, TAsap3DiagHdl Handle, unsigned long ResponseID, char* ParameterName, char* SubParam, unsigned long Iteration)
{
    if (Handle == 0)
        return false;

    DWORD Size = 0;
    char* Value = 0;
    // Call this function first with Value=NULL to get the necessary size of the char array
    if (!Asap3DiagGetComplexStringResponseParameter(hdl, Handle, ParameterName, ResponseID, SubParam, Iteration, Value, &Size)) {
        cout << "Asap3DiagGetComplexStringResponseParameter()-Error" << endl;
        cout << "Last error = " << Asap3GetLastError(hdl) << endl;
        return false;
    }

    if (Size == 0)
        return false;

    Value = new char[Size + 1];
    memset(Value, 0, Size + 1);
    // Now receive the parameter data

    if (!Asap3DiagGetComplexStringResponseParameter(hdl, Handle, ParameterName, ResponseID, SubParam, Iteration, Value, &Size)) {
        cout << "Asap3DiagGetComplexStringResponseParameter()-Error" << endl;
        cout << "Last error = " << Asap3GetLastError(hdl) << endl;
        delete[]Value;
        return false;
    }

    cout << ParameterName << "\\" << SubParam << ": " << Value << endl;
    delete[]Value;
    return true;
}

int DiagnosticExecute(TAsap3Hdl hdl, TAsap3DiagHdl Handle)
{
    if (Handle == 0)
        return false;
    HANDLE hEvent;

    hEvent = CreateEvent(NULL, FALSE, FALSE, NULL);
    Asap3DiagSetNotificationParameters(hdl, Handle, fnDiagNotification, hEvent);
    if (!Asap3DiagExecute(hdl, Handle, FALSE)) {
        cout << "Asap3DiagExecute()-Error" << endl;
        cout << "Last error = " << Asap3GetLastError(hdl) << endl;
        return 0;
    }

    WaitForSingleObject(hEvent, INFINITE);
    CloseHandle(hEvent);
    cout << "Service finished" << endl;


    unsigned int  Responses = 0;
    if (!Asap3DiagGetResponseCount(hdl, Handle, &Responses)) {
        cout << "Asap3DiagCreateSymbolicRequest()-Error" << endl;
        cout << "Last error = " << Asap3GetLastError(hdl) << endl;
        return 0;
    }
    else {
        cout << "Service has " << Responses << " Responses" << endl;
    }
    return Responses;
}

void DiagnosticGetRawStream(TAsap3Hdl hdl, TAsap3DiagHdl Handle, long ID)
{
    eServiceStates State;
    if (!Asap3DiagGetServiceState(hdl, Handle, &State)) {
        cout << "Asap3DiagGetServiceState()-Error" << endl;
        cout << "Last error = " << Asap3GetLastError(hdl) << endl;
        return;
    }
    if (State != e_Finished) {
        cout << "Service isn't finished..." << endl;
    }


    DWORD Size = 0;
    BYTE* Response = 0;

    if (!Asap3DiagGetResponseStream(hdl, Handle, 0, &Size, ID)) {
        cout << "Asap3DiagGetResponseStream()-Error" << endl;
        cout << "Last error = " << Asap3GetLastError(hdl) << endl;
        return;
    }

    Response = new BYTE[Size + 1];
    memset(Response, 0, Size + 1);

    if (!Asap3DiagGetResponseStream(hdl, Handle, Response, &Size, ID)) {
        cout << "Asap3DiagGetResponseStream()-Error" << endl;
        cout << "Last error = " << Asap3GetLastError(hdl) << endl;
        delete[]Response;
        return;
    }
    printf("Raw Response:\r\n");
    for (DWORD i = 0; i < Size; i++) {
        printf("%0X ", Response[i]);
    }
    printf("\r\n");
    delete[]Response;
    return;
}

void DiagnosticRemoveService(TAsap3Hdl hdl, TAsap3DiagHdl Handle)
{

    eServiceStates State;
    if (!Asap3DiagGetServiceState(hdl, Handle, &State)) {
        cout << "Asap3DiagGetServiceState()-Error" << endl;
        cout << "Last error = " << Asap3GetLastError(hdl) << endl;
        return;
    }
    if (State != e_Finished) {
        cout << "Service isn't finished..." << endl;
    }
    if (!Asap3DiagReleaseService(hdl, Handle)) {
        cout << "Asap3DiagReleaseService()-Error" << endl;
        cout << "Last error = " << Asap3GetLastError(hdl) << endl;
        return;
    }
    cout << "Service is removed" << endl;
    return;
}

static void ReadCalValue(TAsap3Hdl Hdl, TModulHdl module, char* name, char* newVal) {
    TCalibrationObjectValue value;

    // ------------------------------------------
    // Kennwert/Parameter lesen und schreiben
    // ------------------------------------------
    value.value.value = 0;

    if (!Asap3ReadCalibrationObject(Hdl, module, name, PHYSICAL_REPRESENTATION,
        &value)) {
        cout << "Asap3ReadCalibrationObject()-Fehler" << endl;
        cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
    }
    else {

        //    cout << "Asap3ReadCalibrationObject executed: " << endl;
        if (value.type == VALUE) {
            cout << "\"" << name << "\":" << " type = " << value.type << " / value = " << value.value.value << endl;

            double _dnewval;
            if (newVal && sscanf(newVal, "%lf", &_dnewval) == 1) {

                value.value.value = _dnewval;

                if (!Asap3WriteCalibrationObject(Hdl, module, name, PHYSICAL_REPRESENTATION,
                    &value)) {
                    cout << "Asap3WriteCalibrationObject()-Fehler" << endl;
                    cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
                }
                else {
                    // Sollte behoben sein!!
                    // sleep(1);  // Read geht während der Messung erst mit Verzögerung; sonst Fehlermeldung
                    if (!Asap3ReadCalibrationObject(Hdl, module, name, PHYSICAL_REPRESENTATION,
                        &value)) {
                        cout << "Asap3ReadCalibrationObject()-Fehler" << endl;
                        cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
                    }
                    else {
                        cout << "New value of \"" << name << "\" = " << value.value.value << endl;
                    }
                }
            }
        }
        else if (value.type == ASCII) {
            char buf[256];
            sprintf(buf, "%*.*s", value.ascii.len, value.ascii.len, value.ascii.ascii);
            cout << "\"" << name << "\":" << " type (ASCII)= " << value.type << " value = \"" << buf << "\"" << endl;
            cout << "len = " << value.ascii.len << endl;

            if (newVal) {
                value.ascii.ascii = newVal;

                if (!Asap3WriteCalibrationObject(Hdl, module, name, PHYSICAL_REPRESENTATION,
                    &value)) {
                    cout << "Asap3WriteCalibrationObject()-Fehler" << endl;
                    cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
                }
                else {
                    // Sollte behoben sein!!
                    // sleep(1);  // Read geht während der Messung erst mit Verzögerung; sonst Fehlermeldung
                    if (!Asap3ReadCalibrationObject(Hdl, module, name, PHYSICAL_REPRESENTATION,
                        &value)) {
                        cout << "Asap3ReadCalibrationObject()-Fehler" << endl;
                        cout << "Last error = " << Asap3GetLastError(Hdl) << endl;
                    }
                    else {
                        sprintf(buf, "%*.*s", value.ascii.len, value.ascii.len, value.ascii.ascii);
                        cout << "New value of \"" << name << "\" = " << buf << endl;
                    }
                }
            }
        }
        else if (value.type == CURVE) {
            int k;
            cout << "\"" << name << "\":" << " type (CURVE)= " << value.type << endl;
            cout << "X    ";
            for (k = 0; k < value.curve.dimension; k++) {
                cout << value.curve.axis[k] << " ";
            }
            cout << endl;
            cout << "W    ";
            for (k = 0; k < value.curve.dimension; k++) {
                cout << value.curve.values[k] << " ";
            }
            cout << endl;
        }
        else if (value.type == MAP) {
            cout << "\"" << name << "\":" << " type (MAP)= " << value.type << endl;
            cout << "Y  /  X" << endl << "       ";
            for (int k = 0; k < value.map.xDimension; k++) {
                cout << value.map.xAxis[k] << " ";
            }
            for (int i = 0; i < value.map.yDimension; i++) {
                cout << endl << value.map.yAxis[i] << "    ";
                for (int j = 0; j < value.map.xDimension; j++) {
                    cout << value.map.values[i * value.map.xDimension + j] << " ";
                }
            }
            cout << endl;
        }
        else if (value.type == VAL_BLK)
        {
            cout << "\"" << name << "\":" << " type (VALBLK)= " << value.type << endl;
            for (int i = 0; i < value.valblk.yDimension; i++) {
                cout << endl;
                for (int j = 0; j < value.valblk.xDimension; j++) {
                    cout << value.valblk.values[i * value.valblk.xDimension + j] << " ";
                }
            }
            cout << endl;
        }
    }
}

static unsigned int Quantisieren(bool incr, unsigned int oldDelay) {
#define MAX_QUANT 22
    static unsigned int quant[MAX_QUANT] = { 10, 15, 20, 30, 40, 60, 80,
                                            100, 150, 200, 300, 400, 600, 800,
                                            1000, 1500, 2000, 3000, 4000, 6000, 8000,
                                            10000 /*, 15000 */ };
    for (int i = 0; i < MAX_QUANT; i++) {
        if (oldDelay == quant[i]) {
            if (i + 1 == MAX_QUANT && incr) return oldDelay;
            else if (i == 0 && !incr)            return oldDelay;
            else                                 return (incr) ? quant[i + 1] : quant[i - 1];
        }
    }
    return 1000;
}


