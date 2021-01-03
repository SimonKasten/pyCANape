#pragma once
#include <pshpack1.h>
#include <stdbool.h>
typedef unsigned long DWORD;
typedef unsigned int UINT;
#define _MAX_PATH 260
#define MAX_PATH 260
#define WINAPI __stdcall
#define AEC_CMD_NOT_SUP               1  
#define AEC_INTERFACE_NOTSUPPORTED    2  
#define AEC_CREATE_MEM_MAPPED_FILE    3  
#define AEC_WRITE_CMD                 4  
#define AEC_READ_RESPONSE             5  
#define AEC_ASAP2_FILE_NOT_FOUND      6  
#define AEC_INVALID_MODULE_HDL        7  
#define AEC_ERR_OPEN_FILE             8  
#define AEC_UNKNOWN_OBJECT            9  
#define AEC_NO_DATABASE               10 
#define AEC_PAR_SIZE_OVERFLOW         11 
#define AEC_NOT_WRITE_ACCESS          12 
#define AEC_OBJECT_TYPE_DOESNT_MATCH  13 
#define AEC_NO_TASKS_OVERFLOW         14 
#define AEC_CCP_RESPONSE_SIZE_INVALID 15 
#define AEC_TIMEOUT_RESPONSE          16 
#define AEC_NO_VALUES_SAMPLED         17 
#define AEC_ACQ_CHNL_OVERRUN          18 
#define AEC_NO_RASTER_OVERFLOW        19 
#define AEC_CANAPE_CREATE_PROC_FAILED 20 
#define AEC_EXIT_DENIED_WHILE_ACQU    21 
#define AEC_WRITE_DATA_FAILED         22 
#define AEC_NO_RESPONSE_FROM_ECU      23 
#define AEC_ACQUIS_ALREADY_RUNNING    24 
#define AEC_ACQUIS_NOT_STARTED        25 
#define AEC_NO_AXIS_PTS_NOT_VALID     27 
#define AEC_SCRIPT_CMD_TO_LARGE       28  
#define AEC_SCRIPT_CMD_INVALID        29  
#define AEC_UNKNOWN_MODULE_NAME       30  
#define AEC_FIFO_INTERNAL_ERROR       31  
#define AEC_VERSION_ERROR             32  
#define AEC_ILLEGAL_DRIVER            33  
#define AEC_CALOBJ_READ_FAILED        34  
#define AEC_ACQ_STP_INIT_FAILED       35  
#define AEC_ACQ_STP_PROC_FAILED       36  
#define AEC_ACQ_STP_OVERFLOW          37  
#define AEC_ACQ_STP_TIME_OVER         38  
#define AEC_NOSERVER_ERRCODE          40  
#define AEC_ERR_OPEN_DATADESCFILE     41  
#define AEC_ERR_OPEN_DATAVERSFILE     42  
#define AEC_TO_MUCH_DISPLAYS_OPEN     43  
#define AEC_INTERNAL_CANAPE_ERROR     44  
#define AEC_CANT_OPEN_DISPLAY         45  
#define AEC_ERR_NO_PATTERNFILE_DEFINED 46 
#define AEC_ERR_OPEN_PATTERNFILE      47  
#define AEC_ERR_CANT_RELEASE_MUTEX    48  
#define AEC_WRONG_CANAPE_VERSION      49  
#define AEC_TCP_SERV_CONNECT_FAILED   50  
#define AEC_TCP_MISSING_CFG           51  
#define AEC_TCP_SERV_NOT_CONNECTED    52  
#define AEC_TCP_EXIT_NOTCLOSED        53
#define AEC_FIFO_ALREADY_INIT         54  
#define AEC_ILLEGAL_OPERATION         55  
#define AEC_WRONG_TYPE                56  
#define AEC_NO_CANAPE_LICENSE         57  
#define AEC_REG_OPEN_KEY_FAILED       58  
#define AEC_REG_QUERY_VALUE_FAILED    59  
#define AEC_WORKDIR_ACCESS_FAILED     60  
#define AEC_INIT_COM_FAILED           61  
#define AEC_INIT_CMD_FAILED           62  
#define AEC_CANAPE_INVALID_PRG_PATH   63  
#define AEC_INVALID_ASAP3_HDL         64  
#define AEC_LOADING_FILE              65  
#define AEC_SAVING_FILE               66  
#define AEC_UPLOAD                    67  
#define AEC_WRITE_VALUE_ERROR         68  
#define AEC_TMTF_NOT_FINSHED          69  
#define AEC_TMTF_SEQUENCE_ERROR       70  
#define AEC_TDBO_TYPE_ERROR           71  
#define AEC_EXECUTE_SERVICE_ERROR     72  
#define AEC_INVALID_DRIVERTYPE        73  
#define AEC_DIAG_INVALID_DRIVERTYPE   74  
#define AEC_DIAG_INVALID_BUSMESSAGE   75  
#define AEC_DIAG_INVALID_VARIANT      76  
#define AEC_DIAG_INVALID_DIAGSERVICE  77  
#define AEC_DIAG_ERR_EXECUTE_SERVICE  78  
#define AEC_DIAG_INVALID_PARAMS       79  
#define AEC_DIAG_UNKNOWN_PARAM_NAME   80  
#define AEC_DIAG_EXCEPTION_ERROR      81  
#define AEC_DIAG_INVALID_RESPONSE     82  
#define AEC_DIAG_UNKNOWN_PARAM_TYPE   83  
#define AEC_DIAG_NO_INFO_AVAILABLE    84  
#define AEC_DIAG_UNKNOWN_RESPHANDLE   85  
#define ACE_DIAG_WRONG_SERVICE_STATE  86  
#define AEC_DIAG_INVALID_INDEX_SIZE   87  
#define AEC_DIAG_INVALID_RESPONSETYPE 88  
#define AEC_FLASH_INVALID_MANAGER     89  
#define AEC_FLASH_OBJ_OUT_OF_RANGE    90  
#define AEC_FLASH_MANAGER_ERROR       91  
#define AEC_FLASH_ALLREADY_RUNNING    92
#define AEC_FLASH_INVALID_APPNAME     93  
#define AEC_FUNCTION_NOT_SUPPORTED    94  
#define AEC_LICENSE_NOT_FOUND         95  
#define AEC_RECORDER_ALLREADY_EXISTS  96  
#define AEC_RECORDER_NOT_FOUND        97  
#define AEC_RECORDER_INDEX_OUTOFRANGE 98  
#define AEC_REMOVE_RECORDER_ERR       99  
#define AEC_INVALID_PARAMETER        100  
#define AEC_ERROR_CREATERECORDER     101  
#define AEC_ERROR_SETRECFILENAME     102  
#define AEC_ERROR_INVALID_TASKID     103  
#define AEC_DIAG_PARAM_SETERROR      104  
#define AEC_CNFG_WRONG_MODE          105  
#define AEC_CNFG_FILE_NOT_FOUND      106  
#define AEC_CNFG_FILE_INVALID        107  
#define AEC_INVALID_SCR_HANDLE       108  
#define AEC_REMOVE_SCR_HANDLE        109  
#define AEC_ERROR_DECALRE_SCR        110  
#define AEC_ERROR_RESUME_SUPPORTED   111  
#define AEC_UNDEFINED_CHANNEL        112  
#define AEC_ERR_DRIVER_CONFIG        113  
#define AEC_ERR_DCB_EXPORT           114  
#define ACE_NOT_AVAILABLE_WHILE_ACQ  115  
#define ACE_NOT_MISSING_LICENSE      116  
#define ACE_EVENT_ALLREADY_REGISERED 117  
#define AEC_OBJECT_ALLREADY_DEFINED  118  
#define AEC_CAL_NOT_ALLOWED          119  
#define AEC_DIAG_UNDEFINED_JOB       120  
#define AEC_ERROR_MODAL_DIALOG       121  
#define AEC_ERROR_CHANNEL_ASSIGNMENT 122  
#define AEC_ERROR_STRUCTURE_OBJECT   123  
#define AEC_NETWORK_NOT_FOUND        124  
#define AEC_ERROR_LOADING_LABELLIST  125  
#define AEC_ERROR_CONV_FILE_ACCESS   126  
#define AEC_ERROR_COMPLEX_RESPONSES  127  
#define AEC_ERROR_INIPATH            128  
#define AEC_USUPPORTED_INTERFACE_ID  129  
#define AEC_INSUFFICENT_BUFFERSIZE   130  
#define AEC_PATCHENTRY_NOT_FOUND     131  
#define AEC_PATCHSECTION_NOT_FOUND   132  
#define AEC_SEC_MANAGER_ERROR        133  
#define ACE_CHANNEL_OPTIMIZED        134  
#define ACE_ERR_PROFILE_ID           135  
#define ACE_ERR_UNSUPPORTED_TYPE     136  
#define AEC_LAST_ERRCODE             137 
enum TApplicationType 
{
  eUNDEFINED   = 0,
  eCANAPE      = 1,    
  eAPPLOCATION = 3     
};
enum TScriptStatus
{
  eTScrReady = 1,      
  eTScrStarting,       
  eTScrRunning,        
  eTScrSleeping,       
  eTScrSuspended,      
  eTScrTerminated,     
  eTScrFinishedReturn, 
  eTScrFinishedCancel, 
  eTScrFailure,        
  eTScrTimeout,        
  eTScrDelayedCompiling, 
                         
  eTScrException       
};
enum e_RamMode
{
  e_TR_MODE_RAM=      0, 
  e_TR_MODE_ROM=      1  
};
enum TRecorderType
{
  eTRecorderTypeMDF         = 0, 
  eTRecorderTypeILinkRT     = 1, 
  eTRecorderTypeBLF         = 2  
};
enum ASAP3_EVENT_CODE
{
  et_ON_DATA_ACQ_START,              
  et_ON_DATA_ACQ_STOP,               
  et_ON_BEFORE_DATA_ACQ_START,       
  et_ON_CLOSEPROJECT,                
  et_ON_OPENPROJECT,                 
  et_ON_CLOSECANAPE                  
};
struct TApplicationID
{
  enum TApplicationType tApplicationType;
  char tApplicationPath[_MAX_PATH];
};
enum TFormat
{
  ECU_INTERNAL = 0,                 
  PHYSICAL_REPRESENTATION = 1,      
};
enum TValueType
{
  VALUE  = 0, 
  CURVE  = 1, 
  MAP    = 2, 
  AXIS   = 3, 
  ASCII  = 4, 
  VAL_BLK= 5  
};
enum TObjectType 
{
  OTT_MEASURE   = 0, 
  OTT_CALIBRATE = 1, 
  OTT_UNKNOWN   = 2  
};
enum eServiceStates
{
 e_Created  =10,             
 e_Running  =e_Created +10,  
 e_Finished =e_Running +10,  
 e_TimeOut  =e_Finished+10   
};
typedef unsigned long TAsap3DiagHdl;
#ifndef EnParamType
enum EnRecorderState
{
 e_RecConfigure, 
 e_RecActive,    
 e_RecRunning,   
 e_RecPaused,    
 e_Suspended     
};
enum EnParamType
{
  ParamSigned     = 1, 
  ParamDouble     = 2, 
  ParamBCD        = 3, 
  ParamUnsigned   = 4, 
  ParamFloat      = 5, 
  ParamAutoDetect = 6  
};
struct DiagJobResponse
{
  char   *job_responsestring; 
  double  job_responseValue;  
};
struct DiagNumericParameter
{
 enum EnParamType DiagNumeric; 
 
 union PValues
 {
  int           IVal;  
  unsigned int  UIVal; 
  float         FVal;  
  double        DVal;  
 };
 union PValues Values;
};
struct DiagNotificationStruct
{
 TAsap3DiagHdl  DiagHandle;    
 enum eServiceStates DiagState;     
 void          *PrivateData;   
};
struct TMeasurementListEntry
{
 unsigned short  taskId;    
 unsigned long   rate;      
 int            SaveFlag;  
 int            Disabled;  
 #if 1
 char           *ObjectName;
 #else
 TReservedOffset_stream ObjectName;
 #endif
};
struct MeasurementListEntries
{
 unsigned int ItemCount;            
 struct TMeasurementListEntry **Entries;   
};
typedef struct DBObjectInfo
{
  enum TObjectType  DBObjecttype; 
  enum TValueType type;           
  double     min;            
  double     max;            
  double     minEx;          
  double     maxEx;          
  unsigned char       precision;      
  char       unit[MAX_PATH]; 
} DBObjectInfo;
struct  DBFileInfo  
{
  char asap2Fname[MAX_PATH]; 
  char asap2Path[MAX_PATH];  
  unsigned char type;                
};
struct TLayoutCoeffs
{
  short OffNx;    
  short OffNy;    
  short OffX;     
  short FakX;     
  short OffY;     
  short FakY;     
  short OffW;     
  short FakWx;    
  short FakWy;    
};
struct SecProfileEntry         
{
  unsigned int mId;            
  char mName[MAX_PATH];        
  char mDescription[MAX_PATH]; 
};
typedef long (CALLBACK* FNCDIAGNOFIFICATION)(unsigned long sizeofstruct, DiagNotificationStruct*);
#endif
 
typedef union { 
  enum TValueType type;
  struct {
    enum TValueType type;
    double value; 
  } value;        
  struct {
    enum TValueType type; 
    short dimension;        
    #if 1
    double*       pAxis;    
    #else
    TReservedOffset_stream axis;
    #endif
    unsigned long oAxis;    
  } axis;      
  struct {        
    enum TValueType type;        
    short len;              
    #if 1
    char*         pAscii;   
    #else
    TReservedOffset_stream ascii;
    #endif
    unsigned long oAscii;   
  } ascii;      
  struct {
    enum TValueType type;
    short dimension;        
    #if 1
    double*       pAxis;    
    #else
    TReservedOffset_stream axis;
    #endif
    unsigned long oAxis;    
    #if 1
    double*       pValues;  
    #else
    TReservedOffset_stream values;
    #endif
    unsigned long oValues;  
  } curve;     
  struct {
    enum TValueType type;
    short xDimension;      
    short yDimension;      
    #if 1
    double*       pXAxis;  
    unsigned long oXAxis;  
    double*       pYAxis;  
    unsigned long oYAxis;  
    double*       pValues; 
    unsigned long oValues; 
    #else
    TReservedOffset_stream xAxis;
    unsigned long oXAxis;
    TReservedOffset_stream yAxis;
    unsigned long oYAxis;
    TReservedOffset_stream values;
    unsigned long oValues;
    #endif
  } map;       
  struct {
    enum TValueType type;
    short xDimension;      
    short yDimension;      
#if 1
    double*       values;  
    unsigned long oValues; 
#else
    TReservedOffset_stream values;
    unsigned long oValues;
#endif
  } valblk;
}
TCalibrationObjectValueEx; 
typedef struct 
{
  #if 1
  double        * xAxisValues; 
  double        * yAxisValues; 
  double        * zValues;     
  double        * zValue;      
  #else
  TReservedOffset_stream xAxisValues;
  TReservedOffset_stream yAxisValues;
  TReservedOffset_stream zValues;
  TReservedOffset_stream zValue;
  #endif
  unsigned long   xStart;      
  unsigned long   yStart;      
  unsigned long   xSize;       
  unsigned long   ySize;       
}
TCalibrationObjectValueEx2; 
typedef union { 
  enum TValueType type;
  struct {
    enum TValueType type;
    double value; 
  } value;        
  struct {
    enum TValueType type; 
    short dimension;       
    #if 1
    double*       axis;    
    #else
    TReservedOffset_stream axis;
    #endif
  } axis;      
  struct {        
    enum TValueType type;        
    short len;              
    #if 1
    char*          ascii;   
    #else
    TReservedOffset_stream ascii;
    #endif
  } ascii;      
  struct {
    enum TValueType type;
    short dimension;        
    #if 1
    double*       axis;    
    double*       values;  
    #else
    TReservedOffset_stream        axis;
    TReservedOffset_stream        values;
    #endif
  } curve;     
  struct {
    enum TValueType type;
    short xDimension;      
    short yDimension;      
    #if 1
    double*       xAxis;  
    double*       yAxis;  
    double*       values; 
    #else
    TReservedOffset_stream        xAxis;
    TReservedOffset_stream        yAxis;
    TReservedOffset_stream        values;
    #endif
  } map;       
  struct {
    enum TValueType type;
    short xDimension;      
    short yDimension;      
#if 1
    double*       values; 
#else
    TReservedOffset_stream        values;
#endif
  } valblk;
}
TCalibrationObjectValue;
 
typedef struct { 
  #if 1
  const char     *description;  
  #else
  TReservedOffset_stream description;
  #endif
  unsigned short  taskId;       
  unsigned long   taskCycle;    
}
TTaskInfo
;
struct TConverterInfo
{ 
  char Comment[_MAX_PATH];  
  char Name   [_MAX_PATH];  
  char ID     [_MAX_PATH];  
};
 
typedef struct {
  #if 1
  const char     *description;  
  #else
  TReservedOffset_stream description;
  #endif
  unsigned short  taskId;       
  unsigned long   taskCycle;    
  unsigned long   eventChannel;
}
TTaskInfo2
;
 
typedef enum  {
  TYPE_FILE,         
  TYPE_VIRTUAL,      
  TYPE_PHYSICAL      
} TAsap3FileType;
typedef enum {
  TYPE_SWITCH_ONLINE,  
  TYPE_SWITCH_OFFLINE, 
}TAsap3ECUState;
typedef enum {
  TYPE_UNKNOWN, 
  TYPE_INT,     
  TYPE_FLOAT,   
  TYPE_DOUBLE,  
  TYPE_SIGNED,  
  TYPE_UNSIGNED,
  TYPE_STRING   
}TAsap3DataType;
typedef enum {
 DBTYPE_MEASUREMENT=1,  
 DBTYPE_CHARACTERISTIC, 
 DBTYPE_ALL             
}TAsap3DBOType;
#define TDBE_VALUE_SCALAR 0x00000001   
#define TDBE_VALUE_CURVE  0x00000002   
#define TDBE_VALUE_MAP    0x00000004   
#define TDBE_VALUE_AXIS   0x00000008   
#define TDBE_VALUE_ASCII  0x00000010   
#define TDBE_VALUE_VALBLK 0x00000020   
#define TDBE_VALUE_ALL    (TDBE_VALUE_SCALAR|TDBE_VALUE_CURVE|TDBE_VALUE_MAP|TDBE_VALUE_AXIS|TDBE_VALUE_ASCII|TDBE_VALUE_VALBLK) 
#define ASAP3_INVALID_HDL (TAsap3Hdl)0          
#define ASAP3_UNUSED_SECURITY (unsigned int)0   
#define ASAP3_NO_SECURITY_JOB ""                
struct tAsap3Hdl;
typedef struct tAsap3Hdl *TAsap3Hdl;

typedef unsigned long *TRecorderID;
#define ASAP3_INVALID_MODULE_HDL (-1) 
typedef unsigned short TModulHdl;
typedef unsigned long  TScriptHdl;
typedef unsigned long TTime;
typedef struct {
  TModulHdl module;         
  unsigned short taskId;    
  unsigned short noSamples; 
} tFifoSize;
typedef struct
{
 unsigned long countOfEntires;  
 unsigned long timestamp;              
 #if 1
 double *data;                  
 #else
 TReservedOffset_stream data;
 #endif
} tSampleObject; 
struct tSampleBlockObject
{
 int has_buffer_Overrun;      
 long has_Error;               
 int initialized;             
 long countofValidEntries;     
 long countofInitilizedEntries;
 struct tSampleObject **tSample;      
};
typedef enum {
  ASAP3_DRIVER_UNKNOWN     = 0,        
  ASAP3_DRIVER_CCP         = 1,        
  ASAP3_DRIVER_XCP         = 2,        
  ASAP3_DRIVER_CAN         = 20,       
  ASAP3_DRIVER_HEXEDIT     = 40,       
  ASAP3_DRIVER_ANALOG      = 50,       
  ASAP3_DRIVER_CANOPEN     = 60,       
  ASAP3_DRIVER_CANDELA     = 70,       
  ASAP3_DRIVER_ENVIRONMENT = 80,       
  ASAP3_DRIVER_LIN         = 90,       
  ASAP3_DRIVER_FLX         = 100,      
  ASAP3_DRIVER_FUNC        = 110,      
  ASAP3_DRIVER_NIDAQMX     = 120,      
  ASAP3_DRIVER_XCP_RAMSCOPE= 130,      
  ASAP3_DRIVER_SYSTEM      = 140,      
  ASAP3_DRIVER_ETH         = 150,      
  ASAP3_DAIO_SYSTEM        = 160,      
  ASAP3_DRIVER_SOME_IP     = 170,      
  ASAP3_DRIVER_DLT         = 180       
} tDriverType;
#ifndef VERSION_T
typedef enum
{
 eT_MEASUREMENT_STOPPED    = 0, 
 eT_MEASUREMENT_INIT       = 1, 
 eT_MEASUREMENT_STOP_ON_START       = 2, 
 eT_MEASUREMENT_EXIT       = 3, 
 eT_MEASUREMENT_THREAD_RUNNING      = 4, 
 eT_MEASUREMENT_RUNNING    = 5  
}tMeasurementState;
#define DLL_INTERFACE_VERSION  "02.03.01.Windows95/WindowsNT.1  "
#define CANAPE_API_MAIN_VESION   2
#define CANAPE_API_SUB_VESION    3
#define CANAPE_API_RELEASE       1
#define CANAPE_API_OS_VERSION    "Windows95/WindowsNT"
#define CANAPE_API_OS_RELEASE    1
#ifndef CUSTOMER_ID
#define CUSTOMER_ID           "Unknown"
#endif
#define VERSION_T
#define MAX_OS_VERSION 50
typedef struct {
  int dllMainVersion; 
  int dllSubVersion;  
  int dllRelease;     
  char osVersion[MAX_OS_VERSION];
  int osRelease;      
} version_t;
#endif
typedef struct {
  int MainVersion;  
  int SubVersion;   
  int ServicePack;  
  char Application[30]; 
} Appversion;
#define   DEV_CAN1        1
#define   DEV_CAN2        2
#define   DEV_CAN3        3
#define   DEV_CAN4        4
#define   DEV_CAN5        5
#define   DEV_CAN6        6
#define   DEV_CAN7        7
#define   DEV_CAN8        8
#define   DEV_CAN20      20
#define   DEV_FLX1       31
#define   DEV_FLX2       32
#define   DEV_FLX3       33
#define   DEV_FLX4       34
#define   DEV_FLX5       35
#define   DEV_FLX6       36
#define   DEV_FLX7       37
#define   DEV_FLX8       38
#define   DEV_LIN1       61
#define   DEV_LIN2       62
#define   DEV_LIN3       63
#define   DEV_LIN4       64
#define   DEV_LIN5       65
#define   DEV_LIN6       66
#define   DEV_LIN7       67
#define   DEV_LIN8       68
#define   DEV_VX_CAN1    81
#define   DEV_VX_CAN2    82
#define   DEV_VX_CAN3    83
#define   DEV_VX_CAN4    84
#define   DEV_VX_TCP     85
#define   DEV_VX_UDP     86
#define   DEV_SXI1       91
#define   DEV_SXI2       92
#define   DEV_SXI3       93
#define   DEV_SXI4       94
#define   DEV_SXI5       95
#define   DEV_SXI6       96
#define   DEV_SXI7       97
#define   DEV_SXI8       98
#define   DEV_USB        110
#define   DEV_CANFD1        121
#define   DEV_CANFD2        122
#define   DEV_CANFD3        123
#define   DEV_CANFD4        124
#define   DEV_CANFD5        125
#define   DEV_CANFD6        126
#define   DEV_CANFD7        127
#define   DEV_CANFD8        128
#define   DEV_CANFD9        129
#define   DEV_TCP         255
#define   DEV_UDP         256
#define   DEV_USERDEFINED 261
#define   DEV_VX_ETHERNET1 271
#define   DEV_VX_ETHERNET2 272
#define   DEV_DAIO_DLL     280
#define ASAP3_EXPORT __declspec(dllexport)
#define CALL_CONV WINAPI
#ifndef _CANAPE_API_TCP_

bool ASAP3_EXPORT CALL_CONV Asap3IsUsCANapeVersion(int *USVersion);
#endif
extern bool ASAP3_EXPORT CALL_CONV Asap3GetVersion(version_t * version);
extern bool ASAP3_EXPORT CALL_CONV Asap3SetTCPOptions(const char* ipAddress, unsigned long portNumber);
extern bool ASAP3_EXPORT CALL_CONV Asap3Init(TAsap3Hdl * hdl,
                                             unsigned long responseTimeout,
                                             const char *workingDir,
                                             unsigned long fifoSize,
                                             bool debugMode);
extern bool ASAP3_EXPORT CALL_CONV Asap3Init2(TAsap3Hdl * hdl,
                                              unsigned long responseTimeout,
                                              const char *workingDir,
                                              unsigned long fifoSize,
                                              unsigned long sampleSize,
                                              bool debugMode);
extern bool ASAP3_EXPORT CALL_CONV Asap3Init3(TAsap3Hdl * hdl,
                                              unsigned long responseTimeout,
                                              const char *workingDir,
                                              unsigned long fifoSize,
                                              unsigned long sampleSize,
                                              bool debugMode,
                                              bool clearDeviceList);
extern bool ASAP3_EXPORT CALL_CONV Asap3Init4(TAsap3Hdl * hdl,
                                              unsigned long responseTimeout,
                                              const char *workingDir,
                                              unsigned long fifoSize,
                                              unsigned long sampleSize,
                                              bool debugMode,
                                              bool clearDeviceList,
                                              bool bHexmode);
extern bool ASAP3_EXPORT CALL_CONV Asap3Init5(TAsap3Hdl * hdl,
                                              unsigned long responseTimeout,
                                              const char *workingDir,
                                              unsigned long fifoSize,
                                              unsigned long sampleSize,
                                              bool debugMode,
                                              bool clearDeviceList,
                                              bool bHexmode,
                                              bool bModalMode);
extern bool ASAP3_EXPORT CALL_CONV Asap3Init6(TAsap3Hdl *hdl,
                                       unsigned long responseTimeout,
                                       const char *projectFile,
                                       unsigned long fifoSize,
                                       unsigned long sampleSize,
                                       bool debugMode,
                                       bool clearDeviceList,
                                       bool bHexmode,
                                       bool bModalMode,
                                       struct TApplicationID  *strApplication);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetProjectDirectory(TAsap3Hdl hdl, char* directory, unsigned long *size);
extern bool ASAP3_EXPORT CALL_CONV Asap3Exit(TAsap3Hdl hdl);
extern unsigned short ASAP3_EXPORT CALL_CONV Asap3GetLastError(TAsap3Hdl hdl);
extern bool ASAP3_EXPORT CALL_CONV Asap3SetApplicationName(TAsap3Hdl hdl, const char *AppName);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetApplicationName(TAsap3Hdl hdl,char *Name,unsigned long *Size);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetApplicationVersion(TAsap3Hdl hdl,Appversion * version);
extern bool ASAP3_EXPORT CALL_CONV Asap3Exit2(TAsap3Hdl hdl,bool close_CANape);
extern bool ASAP3_EXPORT CALL_CONV Asap3ErrorText(TAsap3Hdl hdl, unsigned short errCode, char ** errMsg);
extern bool ASAP3_EXPORT CALL_CONV Asap3PopupDebugWindow(TAsap3Hdl hdl);
extern bool ASAP3_EXPORT CALL_CONV Asap3SaveDebugWindow(TAsap3Hdl hdl, const char *fileName);
extern bool ASAP3_EXPORT CALL_CONV Asap3AttachAsap2(TAsap3Hdl hdl,const char *asap2Fname, short canChnl, TModulHdl * module);
extern bool ASAP3_EXPORT CALL_CONV Asap3CreateModule(TAsap3Hdl hdl, const char *moduleName, const char *databaseFilename,
  short driverType, short channelNo, TModulHdl * module);
extern bool ASAP3_EXPORT CALL_CONV Asap3CreateModule2(TAsap3Hdl hdl, const char *moduleName, const char *databaseFilename,
  short driverType, short channelNo, bool goOnline, TModulHdl * module);
extern bool ASAP3_EXPORT CALL_CONV Asap3CreateModule3(TAsap3Hdl hdl,const char *moduleName, const char *databaseFilename,
  short driverType, short channelNo, bool goOnline, short enablecache, TModulHdl * module);
extern bool ASAP3_EXPORT CALL_CONV Asap3CreateModule4(TAsap3Hdl hdl, const char* moduleName, const char* databaseFname,
  short driverType, short channelNo, const char* interfaceName, bool goOnline, short enableCache, TModulHdl* module);
extern bool ASAP3_EXPORT CALL_CONV Asap3CreateModuleSec(TAsap3Hdl hdl, const char* moduleName, const char* databaseFname,
  short driverType, short channelNo, const char* interfaceName, unsigned int secProfileId, const char* securityRole,
  bool goOnline, short enableCache, TModulHdl* module);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetModuleSecJobName(TAsap3Hdl hdl, TModulHdl module, char* jobName, DWORD* sizeofBuffer);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetModuleCount(TAsap3Hdl hdl,unsigned long *count);
extern bool ASAP3_EXPORT CALL_CONV Asap3RestartMeasurementOnError(TAsap3Hdl hdl,TModulHdl module,bool restart);
extern bool ASAP3_EXPORT CALL_CONV Asap3IsRestartMeasurementOnErrorEnabled(TAsap3Hdl hdl,TModulHdl module,bool *restart);
extern bool ASAP3_EXPORT CALL_CONV Asap3IsModuleActive(TAsap3Hdl hdl,TModulHdl module,bool *activate);
extern bool ASAP3_EXPORT CALL_CONV Asap3ModuleActivation(TAsap3Hdl hdl,TModulHdl module,bool activate);
extern bool ASAP3_EXPORT CALL_CONV Asap3SwitchToMemoryPage(TAsap3Hdl hdl,TModulHdl module,enum e_RamMode mode);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetMemoryPage(TAsap3Hdl hdl,TModulHdl module,enum e_RamMode *mode);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetDBObjectUnit(TAsap3Hdl hdl,TModulHdl module,char *DatabaseObjectName,char *UnitName,UINT *Size);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetDBObjectInfo(TAsap3Hdl hdl,TModulHdl module,char *ObjectName,DBObjectInfo *Info);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetDatabaseObjects(TAsap3Hdl hdl,TModulHdl module,char *DataObjects,UINT *MaxSize,TAsap3DBOType DbType);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetDatabaseObjectsByType(TAsap3Hdl hdl,TModulHdl module,char *DataObjects,UINT *MaxSize,TAsap3DBOType DbType,unsigned long TypeFilter);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetAsap2(TAsap3Hdl hdl, TModulHdl module, char ** asap2Fname);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetDatabaseInfo(TAsap3Hdl hdl, TModulHdl module, struct DBFileInfo *Info) ;
extern bool ASAP3_EXPORT CALL_CONV Asap3TransmitFile2ClientPc(TAsap3Hdl hdl, char *srcFname, char *dstFname);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetModuleName(TAsap3Hdl hdl, TModulHdl module, char **moduleName);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetModuleHandle(TAsap3Hdl hdl, const char *moduleName, TModulHdl * module);
extern bool ASAP3_EXPORT CALL_CONV Asap3ReleaseModule(TAsap3Hdl hdl, TModulHdl module);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetCommunicationType(TAsap3Hdl hdl, TModulHdl module, char ** commType);
bool ASAP3_EXPORT CALL_CONV Asap3ECUOnOffline(TAsap3Hdl hdl, TModulHdl module,TAsap3ECUState State,bool download);
bool ASAP3_EXPORT CALL_CONV Asap3IsECUOnline(TAsap3Hdl hdl, TModulHdl module,TAsap3ECUState *State);
extern bool ASAP3_EXPORT CALL_CONV Asap3ReadByAddress(TAsap3Hdl hdl, TModulHdl module,
                   unsigned long addr, unsigned char addrExt,
                   unsigned long size, unsigned char * data);
extern bool ASAP3_EXPORT CALL_CONV Asap3WriteByAddress(TAsap3Hdl hdl, TModulHdl module,
                   unsigned long addr, unsigned char addrExt,
                   unsigned long size, unsigned char * data);
extern bool ASAP3_EXPORT CALL_CONV Asap3ReadCalibrationObject(TAsap3Hdl hdl, TModulHdl module,
                   const char *calibrationObjectName, enum TFormat format,
                   TCalibrationObjectValue * value);
extern bool ASAP3_EXPORT CALL_CONV Asap3ReadCalibrationObject2(TAsap3Hdl hdl, TModulHdl module,
                   const char *calibrationObjectName,
                   enum TFormat format, bool forceupload,TCalibrationObjectValue *value);
extern bool ASAP3_EXPORT CALL_CONV Asap3ReadCalibrationObjectEx(TAsap3Hdl hdl, TModulHdl module,
                   const char *calibrationObjectName, enum TFormat format,
                   TCalibrationObjectValueEx * value);
extern bool ASAP3_EXPORT CALL_CONV Asap3WriteCalibrationObject(TAsap3Hdl hdl, TModulHdl module,
                   const char *calibrationObjectName, enum TFormat format,
                   TCalibrationObjectValue * value);
extern bool ASAP3_EXPORT CALL_CONV Asap3WriteCalibrationObjectEx(TAsap3Hdl hdl, TModulHdl module,
                   const char *calibrationObjectName, enum TFormat format,
                   TCalibrationObjectValueEx * value);
extern bool ASAP3_EXPORT CALL_CONV Asap3TestObject(TAsap3Hdl hdl, TModulHdl module,
                   const char * objectName, enum TObjectType * type);
extern bool ASAP3_EXPORT CALL_CONV Asap3CalibrationObjectInfo(TAsap3Hdl hdl, TModulHdl module,
                   const char *calibrationObjectName,
                   short * xDimension, short * yDimension);
extern bool ASAP3_EXPORT CALL_CONV Asap3CalibrationObjectInfoEx(TAsap3Hdl hdl, TModulHdl module,
                   const char *calibrationObjectName,
                   short *xDimension, short *yDimension,enum TValueType *type);
extern bool ASAP3_EXPORT CALL_CONV Asap3CalibrationObjectRecordInfo(TAsap3Hdl hdl, TModulHdl module,
                   const char *calibrationObjectName, struct TLayoutCoeffs * coeffs,
                   short * xDimension, short * yDimension);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetEcuTasks(TAsap3Hdl hdl, TModulHdl module,
                   TTaskInfo * taskInfo, unsigned short * noTasks,
                   unsigned short maxTaskInfo);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetEcuTasks2(TAsap3Hdl hdl, TModulHdl module,
                   TTaskInfo2 * taskInfo2, unsigned short *noTasks,
                   unsigned short maxTaskInfo);
extern bool ASAP3_EXPORT CALL_CONV Asap3CreateLoggerConfiguration(TAsap3Hdl hdl,TModulHdl module);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetEcuDriverType(TAsap3Hdl hdl, TModulHdl module,tDriverType *DriverType);
extern bool ASAP3_EXPORT CALL_CONV Asap3HasResumeMode(TAsap3Hdl hdl,TModulHdl module,bool *possible);
extern bool ASAP3_EXPORT CALL_CONV Asap3SetResumeMode(TAsap3Hdl hdl,TModulHdl module);
extern bool ASAP3_EXPORT CALL_CONV Asap3IsResumeModeActive(TAsap3Hdl hdl,TModulHdl module,bool *enabled);
extern bool ASAP3_EXPORT CALL_CONV Asap3ClearResumeMode(TAsap3Hdl hdl,TModulHdl module);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetChnlDefaultRaster(TAsap3Hdl hdl,  TModulHdl module,const char *measurementObjectName,unsigned short *taskId,unsigned short *downSampling);
extern bool ASAP3_EXPORT CALL_CONV Asap3SetupFifo(TAsap3Hdl hdl,
                   unsigned short nFifoSize,
                   tFifoSize fifoSize[]);
extern bool ASAP3_EXPORT CALL_CONV Asap3SetupDataAcquisitionChnl(TAsap3Hdl hdl,  TModulHdl module,
                   const char *measurementObjectName,
                   enum TFormat format, unsigned short taskId,
                   unsigned short pollingRate, bool save2File);
extern bool ASAP3_EXPORT CALL_CONV Asap3SetupDataAcquisitionChnl2(TAsap3Hdl hdl,  TModulHdl module,
                   const char *measurementObjectName,
                   enum TFormat format, unsigned short taskId,
                   unsigned short pollingRate, bool save2File,bool transfer_To_Client);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetMeasurementListEntries(TAsap3Hdl hdl,TModulHdl module,struct MeasurementListEntries **Items);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetMeasurementState(TAsap3Hdl hdl,tMeasurementState *State);
extern bool ASAP3_EXPORT CALL_CONV Asap3HasMCD3License(TAsap3Hdl hdl,bool *available);
extern bool ASAP3_EXPORT CALL_CONV Asap3DefineRecorder(TAsap3Hdl hdl,char *RecorderName,TRecorderID * trecorder,enum TRecorderType RecorderType=eTRecorderTypeMDF);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetRecorderType(TAsap3Hdl hdl, TRecorderID recorderID, enum TRecorderType *RecorderType);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetRecorderName(TAsap3Hdl hdl,TRecorderID recorderID,char * recorderName, long *Size);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetRecorderCount(TAsap3Hdl hdl, unsigned long *count);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetRecorderByIndex(TAsap3Hdl hdl, unsigned long index, TRecorderID *recorderID);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetRecorderByName(TAsap3Hdl hdl,char * recordername,TRecorderID *recorderID);
extern bool ASAP3_EXPORT CALL_CONV Asap3SelectRecorder(TAsap3Hdl hdl,TRecorderID recorderID);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetSelectedRecorder(TAsap3Hdl hdl,TRecorderID *recorderID);
extern bool ASAP3_EXPORT CALL_CONV Asap3RemoveRecorder(TAsap3Hdl hdl,TRecorderID recorderID);                                                
extern bool ASAP3_EXPORT CALL_CONV Asap3EnableBusLoggingRecorderByModule(TAsap3Hdl hdl,  TRecorderID recorderID, TModulHdl module, int enable);
extern bool ASAP3_EXPORT CALL_CONV Asap3EnableBusLoggingRecorderByNetWork(TAsap3Hdl hdl, TRecorderID recorderID, char* NetworkName, int enable);
extern bool ASAP3_EXPORT CALL_CONV Asap3IsRecorderBusLoggingEnableByNetWork(TAsap3Hdl hdl, TRecorderID recorderID, char* NetworkName, int *enable);
extern bool ASAP3_EXPORT CALL_CONV Asap3IsRecorderBusLoggingEnableByModule(TAsap3Hdl hdl, TRecorderID recorderID, TModulHdl module, int *enable);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetRecorderMdfFileName(TAsap3Hdl hdl,TRecorderID recorderID,char *FileName,DWORD *size);
extern bool ASAP3_EXPORT CALL_CONV Asap3SetRecorderMdfFileName(TAsap3Hdl hdl,TRecorderID recorderID,char *FileName);
extern bool ASAP3_EXPORT CALL_CONV Asap3SetRecorderDataReduction(TAsap3Hdl hdl,TRecorderID recorderID,int Reduction);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetRecorderDataReduction(TAsap3Hdl hdl,TRecorderID recorderID,int *Reduction);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetRecorderState(TAsap3Hdl hdl,TRecorderID recorderID,enum EnRecorderState *State);
extern bool ASAP3_EXPORT CALL_CONV Asap3PauseRecorder(TAsap3Hdl hdl,TRecorderID recorderID,bool Pause);
extern bool ASAP3_EXPORT CALL_CONV Asap3StartRecorder(TAsap3Hdl hdl,TRecorderID recorderID);
extern bool ASAP3_EXPORT CALL_CONV Asap3StopRecorder(TAsap3Hdl hdl,TRecorderID recorderID,bool save2Mdf);
extern bool ASAP3_EXPORT CALL_CONV Asap3EnableRecorder(TAsap3Hdl hdl,TRecorderID recorderID,bool enable);
extern bool ASAP3_EXPORT CALL_CONV Asap3IsRecorderEnabled(TAsap3Hdl hdl,TRecorderID recorderID,bool *enabled);
extern bool ASAP3_EXPORT CALL_CONV Asap3ResetDataAcquisitionChnlsByModule(TAsap3Hdl hdl, TModulHdl hmod);
extern bool ASAP3_EXPORT CALL_CONV Asap3ResetDataAcquisitionChnls(TAsap3Hdl hdl);
extern bool ASAP3_EXPORT CALL_CONV Asap3TimeSync(TAsap3Hdl hdl,bool enabled);
extern bool ASAP3_EXPORT CALL_CONV Asap3IsTimeSyncEnabled(TAsap3Hdl hdl,bool *enabled);
extern bool ASAP3_EXPORT CALL_CONV Asap3StartDataAcquisition(TAsap3Hdl hdl);
extern bool ASAP3_EXPORT CALL_CONV Asap3ConnectDataAcquisition(TAsap3Hdl hdl);
extern bool ASAP3_EXPORT CALL_CONV Asap3StartResumedDataAcquisition(TAsap3Hdl hdl);
extern bool ASAP3_EXPORT CALL_CONV Asap3StopDataAcquisition(TAsap3Hdl hdl);
extern bool ASAP3_EXPORT CALL_CONV Asap3DisconnectDataAcquisition(TAsap3Hdl hdl);
extern long ASAP3_EXPORT CALL_CONV Asap3GetFifoLevel(TAsap3Hdl hdl, TModulHdl module, unsigned short taskId);
extern bool ASAP3_EXPORT CALL_CONV Asap3CheckOverrun(TAsap3Hdl hdl, TModulHdl module, unsigned short taskId, bool resetOverrun);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetNextSample(TAsap3Hdl hdl,
                   TModulHdl module,       
                   unsigned short taskId,  
                   TTime * timeStamp,       
                   double ** values);       
                                           
                                           
extern bool ASAP3_EXPORT CALL_CONV Asap3GetCurrentValues(TAsap3Hdl hdl,
                                TModulHdl _module,      
                                unsigned short taskId, 
                                TTime * timeStamp,      
                                double * values,        
                                                        
                                                        
                                                        
                                unsigned short maxValues);  
bool ASAP3_EXPORT CALL_CONV Asap3GetNextSampleBlock(TAsap3Hdl hdl,
                                TModulHdl _module,                   
                                unsigned short taskId,              
                                long count_of_Samples ,              
                                struct tSampleBlockObject ** values);       
extern bool ASAP3_EXPORT CALL_CONV Asap3UseNAN(TAsap3Hdl hdl,bool use);
extern bool ASAP3_EXPORT CALL_CONV Asap3IsNANUsed(TAsap3Hdl hdl,bool *use);
extern bool ASAP3_EXPORT CALL_CONV Asap3SetMdfFilename(TAsap3Hdl hdl, const char *mdfFilename);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetMdfFilename(TAsap3Hdl hdl, char ** mdfFilename);
extern bool ASAP3_EXPORT CALL_CONV Asap3SelectLabelList(TAsap3Hdl hdl, char *Name, bool includeMeaMode = false, int mode = 1);
extern bool ASAP3_EXPORT CALL_CONV Asap3MatlabConversion(TAsap3Hdl hdl, const char *mdfFilename, const char *matlabFilename);
extern bool ASAP3_EXPORT CALL_CONV Asap3MatlabConversionAsync(TAsap3Hdl hdl, const char *mdfFilename, const char *matlabFilename);
extern bool ASAP3_EXPORT CALL_CONV Asap3MDFConverterCount(TAsap3Hdl hdl,int *count);
extern bool ASAP3_EXPORT CALL_CONV Asap3MDFConvert(TAsap3Hdl hdl,char *converterID ,const char *mdfFilename,const char *destFilename,bool overwrite);
extern bool ASAP3_EXPORT CALL_CONV Asap3MDFConverterInfo(TAsap3Hdl hdl,int index,struct TConverterInfo* item);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetNetworkName(TAsap3Hdl hdl,TModulHdl module,char *Name, unsigned int * sizeofName);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetNetworkDevices(TAsap3Hdl hdl,char *Name, TModulHdl * ModuleArray,unsigned int *count);
extern bool ASAP3_EXPORT CALL_CONV Asap3ActivateNetwork(TAsap3Hdl hdl,char *Name, bool activate);
extern bool ASAP3_EXPORT CALL_CONV Asap3IsNetworkActivated(TAsap3Hdl hdl,char *Name, bool *activated);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetSecProfileCount(TAsap3Hdl hdl, unsigned int* count);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetSecProfileIdentifier(TAsap3Hdl hdl, char* identifiers, DWORD* sizeofBuffer);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetSecProfileInfo(TAsap3Hdl hdl, unsigned int id,struct SecProfileEntry* entry);
extern bool ASAP3_EXPORT CALL_CONV Asap3AddSecProfileToNetwork(TAsap3Hdl hdl, unsigned int profileId, char* networkName);
extern bool ASAP3_EXPORT CALL_CONV Asap3_CCP_Request(TAsap3Hdl hdl,
                         TModulHdl module,
                         const unsigned char *requestData,
                         unsigned long  requestSize,
                         unsigned long  responseTimeout,      
                         unsigned char * responseData,
                         unsigned long  maxResponseSize,
                         unsigned long * responseSize);
extern bool ASAP3_EXPORT CALL_CONV Asap3ExecuteScript(TAsap3Hdl hdl,
                                                      TModulHdl module,
                                                      bool scriptFile,
                                                      const char * script);
extern bool ASAP3_EXPORT CALL_CONV Asap3SelectObjects(TAsap3Hdl hdl, TModulHdl module,
                                       enum TObjectType type, const char *fname);
extern bool ASAP3_EXPORT CALL_CONV Asap3RestoreWndSize(TAsap3Hdl hdl);
extern bool ASAP3_EXPORT CALL_CONV Asap3RestoreWndSize2(TAsap3Hdl hdl, long params);
extern bool ASAP3_EXPORT CALL_CONV Asap3CopyBinaryFile(TAsap3Hdl hdl, TModulHdl module, TAsap3FileType sourcetype, TAsap3FileType desttype, const char *filename);
extern bool ASAP3_EXPORT CALL_CONV Asap3ReadObjectParameter(TAsap3Hdl hdl, TModulHdl module, const char *objectName, enum TFormat format, TAsap3DataType * type, unsigned long * address, double * min, double * max, double * increment);
extern bool ASAP3_EXPORT CALL_CONV Asap3ExecuteScriptEx(TAsap3Hdl hdl,
                                                      TModulHdl module,
                                                      bool scriptFile,
                                                      const char * script,
                                                      TScriptHdl *hScript);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetScriptState (TAsap3Hdl hdl,TScriptHdl hScript,enum TScriptStatus *scrstate,char *textBuffer,DWORD *sizeofbuffer);
extern bool ASAP3_EXPORT CALL_CONV Asap3StopScript     (TAsap3Hdl hdl,TScriptHdl hScript) ;
extern bool ASAP3_EXPORT CALL_CONV Asap3StartScript    (TAsap3Hdl hdl,TScriptHdl hScript,char *Commandline=NULL,TModulHdl moduleHdl=ASAP3_INVALID_MODULE_HDL) ;
extern bool ASAP3_EXPORT CALL_CONV Asap3GetScriptResultValue(TAsap3Hdl hdl,TScriptHdl hScript,double *Value);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetScriptResultString(TAsap3Hdl hdl,TScriptHdl hScript,char*resultString,DWORD *sizeofBuffer);
extern bool ASAP3_EXPORT CALL_CONV Asap3ReleaseScript(TAsap3Hdl hdl,TScriptHdl hScript) ;
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagEnableTesterPresent(TAsap3Hdl hdl, TModulHdl module,bool enable);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagIsTesterPresentEnabled(TAsap3Hdl hdl, TModulHdl module, bool *enabled);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagExecuteJob(TAsap3Hdl hdl, TModulHdl module,char *job,char *commandline,bool reserved,struct DiagJobResponse** jobResponse);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagCreateRawRequest(TAsap3Hdl hdl, TModulHdl module,unsigned char *ServiceBytes,unsigned int length,TAsap3DiagHdl *hDiag);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagCreateRawRequest2(TAsap3Hdl hdl, TModulHdl module,unsigned char *Bytes,unsigned int length,TAsap3DiagHdl *hDiag);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagCreateSymbolicRequest(TAsap3Hdl hdl, TModulHdl module, char *ServiceName,TAsap3DiagHdl *hDiag);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagSetNotificationParameters(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,FNCDIAGNOFIFICATION CallbackFunction,void *PrivateData);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagExecute(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,int SupressPositiveResponse);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetServiceState(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,enum eServiceStates *State);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagReleaseService(TAsap3Hdl hdl,TAsap3DiagHdl hDiag);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagSetStringParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char* ParameterName,char* ParameterValue);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagSetRawParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char* ParameterName,unsigned char* ParameterValue,DWORD Size);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagSetNumericParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char* ParameterName,struct DiagNumericParameter *Parameter);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetResponseCount(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,unsigned int *Count);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagIsPositiveResponse(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,long ResponseID,int *IsPositive);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetResponseStream(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,unsigned char* Stream,DWORD *Size,long ResponseID);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetStringResponseParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char *name,long ResponseID,char *Data,DWORD *Size);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetRawResponseParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char *name,long ResponseID,unsigned char *Data,DWORD *Size);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetNumericResponseParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char *name,long ResponseID,struct DiagNumericParameter *);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagIsComplexResponseParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char *name,long ResponseID,int *IsComplex);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetComplexNumericResponseParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char *name,long ResponseID,char *SubParameter,unsigned long InterationIndex,struct DiagNumericParameter *Parameter);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetComplexStringResponseParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char *name,long ResponseID,char *SubParameter,unsigned long InterationIndex,char *Data,DWORD *Size);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetComplexRawResponseParameter(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char *name,long ResponseID,char *SubParameter,unsigned long InterationIndex,char *Data,DWORD *Size);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetResponseCode(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,long ResponseID,unsigned char *Code);
extern bool ASAP3_EXPORT CALL_CONV Asap3DiagGetComplexIterationCount(TAsap3Hdl hdl,TAsap3DiagHdl hDiag,char *Parameter,long ResponseID,unsigned long *Iteration);
bool ASAP3_EXPORT CALL_CONV Asap3LoadCNAFile(TAsap3Hdl hdl,char* configFileName);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetCNAFilename(TAsap3Hdl hdl,char *FileName,unsigned int *Size);
 
 
extern bool ASAP3_EXPORT CALL_CONV Asap3GetCanapeModuleParam(TAsap3Hdl hdl, TModulHdl module, char *param, char *value, unsigned int *sizeofValue);
 
extern bool ASAP3_EXPORT CALL_CONV Asap3SetCanapeModuleParam(TAsap3Hdl hdl, TModulHdl module, char* param, char *value);
 
 
extern bool ASAP3_EXPORT CALL_CONV Asap3GetCanapeProjectParam(TAsap3Hdl hdl, char *Section, char *param, char *value, unsigned int *sizeofValue);
extern bool ASAP3_EXPORT CALL_CONV Asap3SetCanapeProjectParam(TAsap3Hdl hdl, char *Section, char *param, char* value);
extern bool ASAP3_EXPORT CALL_CONV Asap3FlashSetODXContainer(TAsap3Hdl hdl,TModulHdl module,const char *ODXContainerfile);
extern bool ASAP3_EXPORT CALL_CONV Asap3FlashGetSessionCount(TAsap3Hdl hdl,TModulHdl module,unsigned long *Count);
extern bool ASAP3_EXPORT CALL_CONV Asap3FlashGetSessionName(TAsap3Hdl hdl,TModulHdl module,unsigned long index,char *Name,long *SizeOfName);
extern bool ASAP3_EXPORT CALL_CONV Asap3FlashGetJobCount(TAsap3Hdl hdl,TModulHdl module,unsigned long *Count);
extern bool ASAP3_EXPORT CALL_CONV Asap3FlashGetJobName(TAsap3Hdl hdl,TModulHdl module,unsigned long index,char *Name,long *SizeOfName);
extern bool ASAP3_EXPORT CALL_CONV Asap3FlashStartFlashJob(TAsap3Hdl hdl,TModulHdl module,const char *SessionName, const char *JobName, const char *ConfigFileName);
extern bool ASAP3_EXPORT CALL_CONV Asap3FlashGetJobState(TAsap3Hdl hdl,TModulHdl module,double *ScriptResult,int *isRunning,long *Progress,char *Info,unsigned long *SizeofInfo);
extern bool ASAP3_EXPORT CALL_CONV Asap3FlashStopJob(TAsap3Hdl hdl,TModulHdl module);
extern bool ASAP3_EXPORT CALL_CONV Asap3SetInteractiveMode(TAsap3Hdl hdl,bool mode);
extern bool ASAP3_EXPORT CALL_CONV Asap3GetInteractiveMode(TAsap3Hdl hdl,bool *mode);
extern bool ASAP3_EXPORT CALL_CONV Asap3RegisterCallBack(TAsap3Hdl hdl,enum ASAP3_EVENT_CODE eventID,void *fnc,unsigned long privateData);
extern bool ASAP3_EXPORT CALL_CONV Asap3UnRegisterCallBack(TAsap3Hdl hdl,enum ASAP3_EVENT_CODE eventID);
typedef long (CALLBACK* ONMEASUERMENT_START)        (TAsap3Hdl Hdl,unsigned long privateData);
typedef long (CALLBACK* ONMEASUERMENT_STOP)         (TAsap3Hdl Hdl,unsigned long privateData);
typedef long (CALLBACK* ONMEASUERMENT_BEFORE_START) (TAsap3Hdl Hdl,unsigned long privateData);
typedef long (CALLBACK* ON_EXIT)                   (TAsap3Hdl Hdl,unsigned long privateData);
extern bool ASAP3_EXPORT CALL_CONV Asap3ConnectToCANape(TAsap3Hdl *hdl, const char *VillaRelease, const char *Directory, const char *language);
extern bool ASAP3_EXPORT CALL_CONV Asap3DisconnectFromCANape(TAsap3Hdl hdl);
extern bool ASAP3_EXPORT CALL_CONV Asap3OpenDisplayForFile(TAsap3Hdl hdl,const char *Patternfile);
extern bool ASAP3_EXPORT CALL_CONV Asap3ReleaseResultList(TAsap3Hdl hdl,const int CountResults, const char *ResultList[]);
extern bool ASAP3_EXPORT CALL_CONV Asap3OpenDisplay ( TAsap3Hdl hdl, const char *Title,
                                                       int         Editable,
                                                       int         Graphical,
                                                       int         CountParameterLabelsList,
                                                       const char *ParameterLabelList[],
                                                       const char *DataDescFile,
                                                       const char *DataVersFile,
                                                       int         CountAppHistList,
                                                       const char *AppHistLabelList[],
                                                       const char *AppHistTextList[],
                                                       const char *AppHistDefault,
                                                       int        *CountModified,
                                                       const char **ModifiedLabelList[],
                                                       int         *CountErrors,
                                                       const char **ErrorLabelList[],
                                                       int         *CountModAppList,
                                                       const char **ModAppHistLabelList[],
                                                       const char **ModAppHistTextList[]);
extern void ASAP3_EXPORT dummy();
#include <poppack.h>
