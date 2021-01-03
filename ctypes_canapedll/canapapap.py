
import ctypes
import CANapAPI   
import time
  
lib = CANapAPI._libs['CANapAPI64.dll']      


dll_version_t = CANapAPI.version_t(0,0,0,b'null',0) 

lib.Asap3GetVersion.restype = ctypes.c_bool 
ret = lib.Asap3GetVersion(ctypes.byref(dll_version_t))

print(dll_version_t.osVersion)
print(ret)

# äqvivalenter C Code:
# CANapAPI.tAsap3Hdl                           #=> struct tAsap3Hdl;  
TAsap3Hdl = ctypes.POINTER(CANapAPI.tAsap3Hdl)##=> typedef struct tAsap3Hdl *TAsap3Hdl;
Hdl = TAsap3Hdl()#                             #=> TAsap3Hdl Hdl = NULL;

lib.Asap3Init5.argtypes = ctypes.POINTER(TAsap3Hdl), ctypes.c_uint32, ctypes.c_char_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_bool
lib.Asap3Init5.restype = ctypes.c_bool
responseTimeout = ctypes.c_uint32(200000)
workingDir = ctypes.c_char_p(b"C:\\Users\\Public\\Documents\\Vector CANape 19.0\\ExampleDAQXCPSys")
fifoSize = ctypes.c_uint32(8000)
sampleSize = ctypes.c_uint32(320)
debugMode = ctypes.c_bool(True)
clearDeviceList = ctypes.c_bool(False)
bHexmode = ctypes.c_bool(False)
bModalMode = ctypes.c_bool(True)

print('infos: ', Hdl)
# dont know why 'Hdl' gets converted into PointerPointer, probably by argtypes of fcn
ret = lib.Asap3Init5(Hdl, responseTimeout, workingDir, fifoSize, sampleSize, debugMode, clearDeviceList, bHexmode, bModalMode)
print('infos: ', Hdl)

time.sleep(2)

lib.Asap3PopupDebugWindow.argtype = TAsap3Hdl
lib.Asap3PopupDebugWindow.restype = ctypes.c_bool

lib.Asap3PopupDebugWindow(Hdl)


time.sleep(10)

lib.Asap3Exit.argtype = TAsap3Hdl
lib.Asap3Exit.restype = ctypes.c_bool

# Pass in TAsap3Hdl Instance (aka tAsap3Hdl pointer) to Asap3Exit
ret = lib.Asap3Exit(Hdl)



print("done")

