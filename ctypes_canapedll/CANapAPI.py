r"""Wrapper for CANapAPI_stripped.h

Generated with:
C:\Users\sim\AppData\Local\Programs\Python\Python38\Scripts\ctypesgen -a -l CANapAPI64.dll -o CANapAPI.py .\CANapAPI_stripped.h

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python v(3, 2)

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types


class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, Union):

    _fields_ = [("raw", POINTER(c_char)), ("data", c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from c_char array
        elif isinstance(obj, c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util


def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []


class LibraryLoader(object):
    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup(object):
        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            try:
                return self.Lookup(path)
            except:
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # then we search the directory where the generated python interface is stored
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, libname):
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir, name)

    def getdirs(self, libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser("~/lib"), "/usr/local/lib", "/usr/lib"]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        if hasattr(sys, "frozen") and sys.frozen == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    class _Directories(dict):
        def __init__(self):
            self.order = 0

        def add(self, directory):
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            o = self.setdefault(directory, self.order)
            if o == self.order:
                self.order += 1

        def extend(self, directories):
            for d in directories:
                self.add(d)

        def ordered(self):
            return (i[0] for i in sorted(self.items(), key=lambda D: D[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive funtion to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as f:
                for D in f:
                    D = D.strip()
                    if not D:
                        continue

                    m = self._include.match(D)
                    if not m:
                        dirs.add(D)
                    else:
                        for D2 in glob.glob(m.group("pattern")):
                            self._get_ld_so_conf_dirs(D2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HPUX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/x86_64-linux-gnu", "/usr/lib/x86_64-linux-gnu"]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        ext_re = re.compile(r"\.s[ol]$")
        for dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for F in other_dirs:
        if not os.path.isabs(F):
            F = os.path.abspath(F)
        load_library.other_dirs.append(F)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["CANapAPI64.dll"] = load_library("CANapAPI64.dll")

# 1 libraries
# End libraries

# No modules

DWORD = c_ulong# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 4

UINT = c_uint# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 5

enum_TApplicationType = c_int# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 144

eUNDEFINED = 0# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 144

eCANAPE = 1# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 144

eAPPLOCATION = 3# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 144

enum_TScriptStatus = c_int# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 150

eTScrReady = 1# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 150

eTScrStarting = (eTScrReady + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 150

eTScrRunning = (eTScrStarting + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 150

eTScrSleeping = (eTScrRunning + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 150

eTScrSuspended = (eTScrSleeping + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 150

eTScrTerminated = (eTScrSuspended + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 150

eTScrFinishedReturn = (eTScrTerminated + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 150

eTScrFinishedCancel = (eTScrFinishedReturn + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 150

eTScrFailure = (eTScrFinishedCancel + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 150

eTScrTimeout = (eTScrFailure + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 150

eTScrDelayedCompiling = (eTScrTimeout + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 150

eTScrException = (eTScrDelayedCompiling + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 150

enum_e_RamMode = c_int# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 166

e_TR_MODE_RAM = 0# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 166

e_TR_MODE_ROM = 1# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 166

enum_TRecorderType = c_int# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 171

eTRecorderTypeMDF = 0# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 171

eTRecorderTypeILinkRT = 1# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 171

eTRecorderTypeBLF = 2# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 171

enum_ASAP3_EVENT_CODE = c_int# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 177

et_ON_DATA_ACQ_START = 0# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 177

et_ON_DATA_ACQ_STOP = (et_ON_DATA_ACQ_START + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 177

et_ON_BEFORE_DATA_ACQ_START = (et_ON_DATA_ACQ_STOP + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 177

et_ON_CLOSEPROJECT = (et_ON_BEFORE_DATA_ACQ_START + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 177

et_ON_OPENPROJECT = (et_ON_CLOSEPROJECT + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 177

et_ON_CLOSECANAPE = (et_ON_OPENPROJECT + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 177

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 186
class struct_TApplicationID(Structure):
    pass

struct_TApplicationID._pack_ = 1
struct_TApplicationID.__slots__ = [
    'tApplicationType',
    'tApplicationPath',
]
struct_TApplicationID._fields_ = [
    ('tApplicationType', enum_TApplicationType),
    ('tApplicationPath', c_char * int(260)),
]

enum_TFormat = c_int# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 191

ECU_INTERNAL = 0# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 191

PHYSICAL_REPRESENTATION = 1# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 191

enum_TValueType = c_int# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 196

VALUE = 0# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 196

CURVE = 1# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 196

MAP = 2# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 196

AXIS = 3# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 196

ASCII = 4# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 196

VAL_BLK = 5# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 196

enum_TObjectType = c_int# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 205

OTT_MEASURE = 0# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 205

OTT_CALIBRATE = 1# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 205

OTT_UNKNOWN = 2# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 205

enum_eServiceStates = c_int# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 211

e_Created = 10# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 211

e_Running = (e_Created + 10)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 211

e_Finished = (e_Running + 10)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 211

e_TimeOut = (e_Finished + 10)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 211

TAsap3DiagHdl = c_ulong# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 218

enum_EnRecorderState = c_int# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 220

e_RecConfigure = 0# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 220

e_RecActive = (e_RecConfigure + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 220

e_RecRunning = (e_RecActive + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 220

e_RecPaused = (e_RecRunning + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 220

e_Suspended = (e_RecPaused + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 220

enum_EnParamType = c_int# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 228

ParamSigned = 1# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 228

ParamDouble = 2# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 228

ParamBCD = 3# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 228

ParamUnsigned = 4# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 228

ParamFloat = 5# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 228

ParamAutoDetect = 6# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 228

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 237
class struct_DiagJobResponse(Structure):
    pass

struct_DiagJobResponse._pack_ = 1
struct_DiagJobResponse.__slots__ = [
    'job_responsestring',
    'job_responseValue',
]
struct_DiagJobResponse._fields_ = [
    ('job_responsestring', String),
    ('job_responseValue', c_double),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 246
class union_PValues(Union):
    pass

union_PValues._pack_ = 1
union_PValues.__slots__ = [
    'IVal',
    'UIVal',
    'FVal',
    'DVal',
]
union_PValues._fields_ = [
    ('IVal', c_int),
    ('UIVal', c_uint),
    ('FVal', c_float),
    ('DVal', c_double),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 242
class struct_DiagNumericParameter(Structure):
    pass

struct_DiagNumericParameter._pack_ = 1
struct_DiagNumericParameter.__slots__ = [
    'DiagNumeric',
    'unnamed_1',
    'Values',
]
struct_DiagNumericParameter._anonymous_ = [
    'unnamed_1',
]
struct_DiagNumericParameter._fields_ = [
    ('DiagNumeric', enum_EnParamType),
    ('unnamed_1', union_PValues),
    ('Values', union_PValues),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 255
class struct_DiagNotificationStruct(Structure):
    pass

struct_DiagNotificationStruct._pack_ = 1
struct_DiagNotificationStruct.__slots__ = [
    'DiagHandle',
    'DiagState',
    'PrivateData',
]
struct_DiagNotificationStruct._fields_ = [
    ('DiagHandle', TAsap3DiagHdl),
    ('DiagState', enum_eServiceStates),
    ('PrivateData', POINTER(None)),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 261
class struct_TMeasurementListEntry(Structure):
    pass

struct_TMeasurementListEntry._pack_ = 1
struct_TMeasurementListEntry.__slots__ = [
    'taskId',
    'rate',
    'SaveFlag',
    'Disabled',
    'ObjectName',
]
struct_TMeasurementListEntry._fields_ = [
    ('taskId', c_ushort),
    ('rate', c_ulong),
    ('SaveFlag', c_int),
    ('Disabled', c_int),
    ('ObjectName', String),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 273
class struct_MeasurementListEntries(Structure):
    pass

struct_MeasurementListEntries._pack_ = 1
struct_MeasurementListEntries.__slots__ = [
    'ItemCount',
    'Entries',
]
struct_MeasurementListEntries._fields_ = [
    ('ItemCount', c_uint),
    ('Entries', POINTER(POINTER(struct_TMeasurementListEntry))),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 288
class struct_DBObjectInfo(Structure):
    pass

struct_DBObjectInfo._pack_ = 1
struct_DBObjectInfo.__slots__ = [
    'DBObjecttype',
    'type',
    'min',
    'max',
    'minEx',
    'maxEx',
    'precision',
    'unit',
]
struct_DBObjectInfo._fields_ = [
    ('DBObjecttype', enum_TObjectType),
    ('type', enum_TValueType),
    ('min', c_double),
    ('max', c_double),
    ('minEx', c_double),
    ('maxEx', c_double),
    ('precision', c_ubyte),
    ('unit', c_char * int(260)),
]

DBObjectInfo = struct_DBObjectInfo# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 288

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 289
class struct_DBFileInfo(Structure):
    pass

struct_DBFileInfo._pack_ = 1
struct_DBFileInfo.__slots__ = [
    'asap2Fname',
    'asap2Path',
    'type',
]
struct_DBFileInfo._fields_ = [
    ('asap2Fname', c_char * int(260)),
    ('asap2Path', c_char * int(260)),
    ('type', c_ubyte),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 295
class struct_TLayoutCoeffs(Structure):
    pass

struct_TLayoutCoeffs._pack_ = 1
struct_TLayoutCoeffs.__slots__ = [
    'OffNx',
    'OffNy',
    'OffX',
    'FakX',
    'OffY',
    'FakY',
    'OffW',
    'FakWx',
    'FakWy',
]
struct_TLayoutCoeffs._fields_ = [
    ('OffNx', c_short),
    ('OffNy', c_short),
    ('OffX', c_short),
    ('FakX', c_short),
    ('OffY', c_short),
    ('FakY', c_short),
    ('OffW', c_short),
    ('FakWx', c_short),
    ('FakWy', c_short),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 307
class struct_SecProfileEntry(Structure):
    pass

struct_SecProfileEntry._pack_ = 1
struct_SecProfileEntry.__slots__ = [
    'mId',
    'mName',
    'mDescription',
]
struct_SecProfileEntry._fields_ = [
    ('mId', c_uint),
    ('mName', c_char * int(260)),
    ('mDescription', c_char * int(260)),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 318
class struct_anon_1(Structure):
    pass

struct_anon_1._pack_ = 1
struct_anon_1.__slots__ = [
    'type',
    'value',
]
struct_anon_1._fields_ = [
    ('type', enum_TValueType),
    ('value', c_double),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 322
class struct_anon_2(Structure):
    pass

struct_anon_2._pack_ = 1
struct_anon_2.__slots__ = [
    'type',
    'dimension',
    'pAxis',
    'oAxis',
]
struct_anon_2._fields_ = [
    ('type', enum_TValueType),
    ('dimension', c_short),
    ('pAxis', POINTER(c_double)),
    ('oAxis', c_ulong),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 332
class struct_anon_3(Structure):
    pass

struct_anon_3._pack_ = 1
struct_anon_3.__slots__ = [
    'type',
    'len',
    'pAscii',
    'oAscii',
]
struct_anon_3._fields_ = [
    ('type', enum_TValueType),
    ('len', c_short),
    ('pAscii', String),
    ('oAscii', c_ulong),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 342
class struct_anon_4(Structure):
    pass

struct_anon_4._pack_ = 1
struct_anon_4.__slots__ = [
    'type',
    'dimension',
    'pAxis',
    'oAxis',
    'pValues',
    'oValues',
]
struct_anon_4._fields_ = [
    ('type', enum_TValueType),
    ('dimension', c_short),
    ('pAxis', POINTER(c_double)),
    ('oAxis', c_ulong),
    ('pValues', POINTER(c_double)),
    ('oValues', c_ulong),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 358
class struct_anon_5(Structure):
    pass

struct_anon_5._pack_ = 1
struct_anon_5.__slots__ = [
    'type',
    'xDimension',
    'yDimension',
    'pXAxis',
    'oXAxis',
    'pYAxis',
    'oYAxis',
    'pValues',
    'oValues',
]
struct_anon_5._fields_ = [
    ('type', enum_TValueType),
    ('xDimension', c_short),
    ('yDimension', c_short),
    ('pXAxis', POINTER(c_double)),
    ('oXAxis', c_ulong),
    ('pYAxis', POINTER(c_double)),
    ('oYAxis', c_ulong),
    ('pValues', POINTER(c_double)),
    ('oValues', c_ulong),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 378
class struct_anon_6(Structure):
    pass

struct_anon_6._pack_ = 1
struct_anon_6.__slots__ = [
    'type',
    'xDimension',
    'yDimension',
    'values',
    'oValues',
]
struct_anon_6._fields_ = [
    ('type', enum_TValueType),
    ('xDimension', c_short),
    ('yDimension', c_short),
    ('values', POINTER(c_double)),
    ('oValues', c_ulong),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 391
class union_anon_7(Union):
    pass

union_anon_7._pack_ = 1
union_anon_7.__slots__ = [
    'type',
    'value',
    'axis',
    'ascii',
    'curve',
    'map',
    'valblk',
]
union_anon_7._fields_ = [
    ('type', enum_TValueType),
    ('value', struct_anon_1),
    ('axis', struct_anon_2),
    ('ascii', struct_anon_3),
    ('curve', struct_anon_4),
    ('map', struct_anon_5),
    ('valblk', struct_anon_6),
]

TCalibrationObjectValueEx = union_anon_7# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 391

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 410
class struct_anon_8(Structure):
    pass

struct_anon_8._pack_ = 1
struct_anon_8.__slots__ = [
    'xAxisValues',
    'yAxisValues',
    'zValues',
    'zValue',
    'xStart',
    'yStart',
    'xSize',
    'ySize',
]
struct_anon_8._fields_ = [
    ('xAxisValues', POINTER(c_double)),
    ('yAxisValues', POINTER(c_double)),
    ('zValues', POINTER(c_double)),
    ('zValue', POINTER(c_double)),
    ('xStart', c_ulong),
    ('yStart', c_ulong),
    ('xSize', c_ulong),
    ('ySize', c_ulong),
]

TCalibrationObjectValueEx2 = struct_anon_8# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 410

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 413
class struct_anon_9(Structure):
    pass

struct_anon_9._pack_ = 1
struct_anon_9.__slots__ = [
    'type',
    'value',
]
struct_anon_9._fields_ = [
    ('type', enum_TValueType),
    ('value', c_double),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 417
class struct_anon_10(Structure):
    pass

struct_anon_10._pack_ = 1
struct_anon_10.__slots__ = [
    'type',
    'dimension',
    'axis',
]
struct_anon_10._fields_ = [
    ('type', enum_TValueType),
    ('dimension', c_short),
    ('axis', POINTER(c_double)),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 426
class struct_anon_11(Structure):
    pass

struct_anon_11._pack_ = 1
struct_anon_11.__slots__ = [
    'type',
    'len',
    'ascii',
]
struct_anon_11._fields_ = [
    ('type', enum_TValueType),
    ('len', c_short),
    ('ascii', String),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 435
class struct_anon_12(Structure):
    pass

struct_anon_12._pack_ = 1
struct_anon_12.__slots__ = [
    'type',
    'dimension',
    'axis',
    'values',
]
struct_anon_12._fields_ = [
    ('type', enum_TValueType),
    ('dimension', c_short),
    ('axis', POINTER(c_double)),
    ('values', POINTER(c_double)),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 446
class struct_anon_13(Structure):
    pass

struct_anon_13._pack_ = 1
struct_anon_13.__slots__ = [
    'type',
    'xDimension',
    'yDimension',
    'xAxis',
    'yAxis',
    'values',
]
struct_anon_13._fields_ = [
    ('type', enum_TValueType),
    ('xDimension', c_short),
    ('yDimension', c_short),
    ('xAxis', POINTER(c_double)),
    ('yAxis', POINTER(c_double)),
    ('values', POINTER(c_double)),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 460
class struct_anon_14(Structure):
    pass

struct_anon_14._pack_ = 1
struct_anon_14.__slots__ = [
    'type',
    'xDimension',
    'yDimension',
    'values',
]
struct_anon_14._fields_ = [
    ('type', enum_TValueType),
    ('xDimension', c_short),
    ('yDimension', c_short),
    ('values', POINTER(c_double)),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 471
class union_anon_15(Union):
    pass

union_anon_15._pack_ = 1
union_anon_15.__slots__ = [
    'type',
    'value',
    'axis',
    'ascii',
    'curve',
    'map',
    'valblk',
]
union_anon_15._fields_ = [
    ('type', enum_TValueType),
    ('value', struct_anon_9),
    ('axis', struct_anon_10),
    ('ascii', struct_anon_11),
    ('curve', struct_anon_12),
    ('map', struct_anon_13),
    ('valblk', struct_anon_14),
]

TCalibrationObjectValue = union_anon_15# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 471

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 482
class struct_anon_16(Structure):
    pass

struct_anon_16._pack_ = 1
struct_anon_16.__slots__ = [
    'description',
    'taskId',
    'taskCycle',
]
struct_anon_16._fields_ = [
    ('description', String),
    ('taskId', c_ushort),
    ('taskCycle', c_ulong),
]

TTaskInfo = struct_anon_16# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 482

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 484
class struct_TConverterInfo(Structure):
    pass

struct_TConverterInfo._pack_ = 1
struct_TConverterInfo.__slots__ = [
    'Comment',
    'Name',
    'ID',
]
struct_TConverterInfo._fields_ = [
    ('Comment', c_char * int(260)),
    ('Name', c_char * int(260)),
    ('ID', c_char * int(260)),
]

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 501
class struct_anon_17(Structure):
    pass

struct_anon_17._pack_ = 1
struct_anon_17.__slots__ = [
    'description',
    'taskId',
    'taskCycle',
    'eventChannel',
]
struct_anon_17._fields_ = [
    ('description', String),
    ('taskId', c_ushort),
    ('taskCycle', c_ulong),
    ('eventChannel', c_ulong),
]

TTaskInfo2 = struct_anon_17# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 501

enum_anon_18 = c_int# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 508

TYPE_FILE = 0# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 508

TYPE_VIRTUAL = (TYPE_FILE + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 508

TYPE_PHYSICAL = (TYPE_VIRTUAL + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 508

TAsap3FileType = enum_anon_18# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 508

enum_anon_19 = c_int# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 512

TYPE_SWITCH_ONLINE = 0# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 512

TYPE_SWITCH_OFFLINE = (TYPE_SWITCH_ONLINE + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 512

TAsap3ECUState = enum_anon_19# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 512

enum_anon_20 = c_int# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 521

TYPE_UNKNOWN = 0# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 521

TYPE_INT = (TYPE_UNKNOWN + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 521

TYPE_FLOAT = (TYPE_INT + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 521

TYPE_DOUBLE = (TYPE_FLOAT + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 521

TYPE_SIGNED = (TYPE_DOUBLE + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 521

TYPE_UNSIGNED = (TYPE_SIGNED + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 521

TYPE_STRING = (TYPE_UNSIGNED + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 521

TAsap3DataType = enum_anon_20# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 521

enum_anon_21 = c_int# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 526

DBTYPE_MEASUREMENT = 1# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 526

DBTYPE_CHARACTERISTIC = (DBTYPE_MEASUREMENT + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 526

DBTYPE_ALL = (DBTYPE_CHARACTERISTIC + 1)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 526

TAsap3DBOType = enum_anon_21# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 526

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 537
class struct_tAsap3Hdl(Structure):
    pass

TAsap3Hdl = POINTER(struct_tAsap3Hdl)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 538

TRecorderID = POINTER(c_ulong)# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 547

TModulHdl = c_ushort# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 549

TScriptHdl = c_ulong# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 550

TTime = c_ulong# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 551

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 556
class struct_anon_22(Structure):
    pass

struct_anon_22._pack_ = 1
struct_anon_22.__slots__ = [
    'module',
    'taskId',
    'noSamples',
]
struct_anon_22._fields_ = [
    ('module', TModulHdl),
    ('taskId', c_ushort),
    ('noSamples', c_ushort),
]

tFifoSize = struct_anon_22# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 556

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 566
class struct_anon_23(Structure):
    pass

struct_anon_23._pack_ = 1
struct_anon_23.__slots__ = [
    'countOfEntires',
    'timestamp',
    'data',
]
struct_anon_23._fields_ = [
    ('countOfEntires', c_ulong),
    ('timestamp', c_ulong),
    ('data', POINTER(c_double)),
]

tSampleObject = struct_anon_23# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 566

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 574
class struct_tSampleObject(Structure):
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 567
class struct_tSampleBlockObject(Structure):
    pass

struct_tSampleBlockObject._pack_ = 1
struct_tSampleBlockObject.__slots__ = [
    'has_buffer_Overrun',
    'has_Error',
    'initialized',
    'countofValidEntries',
    'countofInitilizedEntries',
    'tSample',
]
struct_tSampleBlockObject._fields_ = [
    ('has_buffer_Overrun', c_int),
    ('has_Error', c_long),
    ('initialized', c_int),
    ('countofValidEntries', c_long),
    ('countofInitilizedEntries', c_long),
    ('tSample', POINTER(POINTER(struct_tSampleObject))),
]

enum_anon_24 = c_int# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DRIVER_UNKNOWN = 0# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DRIVER_CCP = 1# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DRIVER_XCP = 2# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DRIVER_CAN = 20# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DRIVER_HEXEDIT = 40# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DRIVER_ANALOG = 50# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DRIVER_CANOPEN = 60# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DRIVER_CANDELA = 70# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DRIVER_ENVIRONMENT = 80# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DRIVER_LIN = 90# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DRIVER_FLX = 100# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DRIVER_FUNC = 110# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DRIVER_NIDAQMX = 120# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DRIVER_XCP_RAMSCOPE = 130# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DRIVER_SYSTEM = 140# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DRIVER_ETH = 150# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DAIO_SYSTEM = 160# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DRIVER_SOME_IP = 170# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

ASAP3_DRIVER_DLT = 180# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

tDriverType = enum_anon_24# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 596

enum_anon_25 = c_int# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 606

eT_MEASUREMENT_STOPPED = 0# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 606

eT_MEASUREMENT_INIT = 1# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 606

eT_MEASUREMENT_STOP_ON_START = 2# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 606

eT_MEASUREMENT_EXIT = 3# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 606

eT_MEASUREMENT_THREAD_RUNNING = 4# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 606

eT_MEASUREMENT_RUNNING = 5# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 606

tMeasurementState = enum_anon_25# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 606

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 624
class struct_anon_26(Structure):
    pass

struct_anon_26._pack_ = 1
struct_anon_26.__slots__ = [
    'dllMainVersion',
    'dllSubVersion',
    'dllRelease',
    'osVersion',
    'osRelease',
]
struct_anon_26._fields_ = [
    ('dllMainVersion', c_int),
    ('dllSubVersion', c_int),
    ('dllRelease', c_int),
    ('osVersion', c_char * int(50)),
    ('osRelease', c_int),
]

version_t = struct_anon_26# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 624

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 631
class struct_anon_27(Structure):
    pass

struct_anon_27._pack_ = 1
struct_anon_27.__slots__ = [
    'MainVersion',
    'SubVersion',
    'ServicePack',
    'Application',
]
struct_anon_27._fields_ = [
    ('MainVersion', c_int),
    ('SubVersion', c_int),
    ('ServicePack', c_int),
    ('Application', c_char * int(30)),
]

Appversion = struct_anon_27# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 631

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 691
if _libs["CANapAPI64.dll"].has("Asap3IsUsCANapeVersion", "stdcall"):
    Asap3IsUsCANapeVersion = _libs["CANapAPI64.dll"].get("Asap3IsUsCANapeVersion", "stdcall")
    Asap3IsUsCANapeVersion.argtypes = [POINTER(c_int)]
    Asap3IsUsCANapeVersion.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 693
if _libs["CANapAPI64.dll"].has("Asap3GetVersion", "stdcall"):
    Asap3GetVersion = _libs["CANapAPI64.dll"].get("Asap3GetVersion", "stdcall")
    Asap3GetVersion.argtypes = [POINTER(version_t)]
    Asap3GetVersion.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 694
if _libs["CANapAPI64.dll"].has("Asap3SetTCPOptions", "stdcall"):
    Asap3SetTCPOptions = _libs["CANapAPI64.dll"].get("Asap3SetTCPOptions", "stdcall")
    Asap3SetTCPOptions.argtypes = [String, c_ulong]
    Asap3SetTCPOptions.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 695
if _libs["CANapAPI64.dll"].has("Asap3Init", "stdcall"):
    Asap3Init = _libs["CANapAPI64.dll"].get("Asap3Init", "stdcall")
    Asap3Init.argtypes = [POINTER(TAsap3Hdl), c_ulong, String, c_ulong, c_bool]
    Asap3Init.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 700
if _libs["CANapAPI64.dll"].has("Asap3Init2", "stdcall"):
    Asap3Init2 = _libs["CANapAPI64.dll"].get("Asap3Init2", "stdcall")
    Asap3Init2.argtypes = [POINTER(TAsap3Hdl), c_ulong, String, c_ulong, c_ulong, c_bool]
    Asap3Init2.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 706
if _libs["CANapAPI64.dll"].has("Asap3Init3", "stdcall"):
    Asap3Init3 = _libs["CANapAPI64.dll"].get("Asap3Init3", "stdcall")
    Asap3Init3.argtypes = [POINTER(TAsap3Hdl), c_ulong, String, c_ulong, c_ulong, c_bool, c_bool]
    Asap3Init3.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 713
if _libs["CANapAPI64.dll"].has("Asap3Init4", "stdcall"):
    Asap3Init4 = _libs["CANapAPI64.dll"].get("Asap3Init4", "stdcall")
    Asap3Init4.argtypes = [POINTER(TAsap3Hdl), c_ulong, String, c_ulong, c_ulong, c_bool, c_bool, c_bool]
    Asap3Init4.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 721
if _libs["CANapAPI64.dll"].has("Asap3Init5", "stdcall"):
    Asap3Init5 = _libs["CANapAPI64.dll"].get("Asap3Init5", "stdcall")
    Asap3Init5.argtypes = [POINTER(TAsap3Hdl), c_ulong, String, c_ulong, c_ulong, c_bool, c_bool, c_bool, c_bool]
    Asap3Init5.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 730
if _libs["CANapAPI64.dll"].has("Asap3Init6", "stdcall"):
    Asap3Init6 = _libs["CANapAPI64.dll"].get("Asap3Init6", "stdcall")
    Asap3Init6.argtypes = [POINTER(TAsap3Hdl), c_ulong, String, c_ulong, c_ulong, c_bool, c_bool, c_bool, c_bool, POINTER(struct_TApplicationID)]
    Asap3Init6.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 740
if _libs["CANapAPI64.dll"].has("Asap3GetProjectDirectory", "stdcall"):
    Asap3GetProjectDirectory = _libs["CANapAPI64.dll"].get("Asap3GetProjectDirectory", "stdcall")
    Asap3GetProjectDirectory.argtypes = [TAsap3Hdl, String, POINTER(c_ulong)]
    Asap3GetProjectDirectory.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 741
if _libs["CANapAPI64.dll"].has("Asap3Exit", "stdcall"):
    Asap3Exit = _libs["CANapAPI64.dll"].get("Asap3Exit", "stdcall")
    Asap3Exit.argtypes = [TAsap3Hdl]
    Asap3Exit.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 742
if _libs["CANapAPI64.dll"].has("Asap3GetLastError", "stdcall"):
    Asap3GetLastError = _libs["CANapAPI64.dll"].get("Asap3GetLastError", "stdcall")
    Asap3GetLastError.argtypes = [TAsap3Hdl]
    Asap3GetLastError.restype = c_ushort

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 743
if _libs["CANapAPI64.dll"].has("Asap3SetApplicationName", "stdcall"):
    Asap3SetApplicationName = _libs["CANapAPI64.dll"].get("Asap3SetApplicationName", "stdcall")
    Asap3SetApplicationName.argtypes = [TAsap3Hdl, String]
    Asap3SetApplicationName.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 744
if _libs["CANapAPI64.dll"].has("Asap3GetApplicationName", "stdcall"):
    Asap3GetApplicationName = _libs["CANapAPI64.dll"].get("Asap3GetApplicationName", "stdcall")
    Asap3GetApplicationName.argtypes = [TAsap3Hdl, String, POINTER(c_ulong)]
    Asap3GetApplicationName.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 745
if _libs["CANapAPI64.dll"].has("Asap3GetApplicationVersion", "stdcall"):
    Asap3GetApplicationVersion = _libs["CANapAPI64.dll"].get("Asap3GetApplicationVersion", "stdcall")
    Asap3GetApplicationVersion.argtypes = [TAsap3Hdl, POINTER(Appversion)]
    Asap3GetApplicationVersion.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 746
if _libs["CANapAPI64.dll"].has("Asap3Exit2", "stdcall"):
    Asap3Exit2 = _libs["CANapAPI64.dll"].get("Asap3Exit2", "stdcall")
    Asap3Exit2.argtypes = [TAsap3Hdl, c_bool]
    Asap3Exit2.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 747
if _libs["CANapAPI64.dll"].has("Asap3ErrorText", "stdcall"):
    Asap3ErrorText = _libs["CANapAPI64.dll"].get("Asap3ErrorText", "stdcall")
    Asap3ErrorText.argtypes = [TAsap3Hdl, c_ushort, POINTER(POINTER(c_char))]
    Asap3ErrorText.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 748
if _libs["CANapAPI64.dll"].has("Asap3PopupDebugWindow", "stdcall"):
    Asap3PopupDebugWindow = _libs["CANapAPI64.dll"].get("Asap3PopupDebugWindow", "stdcall")
    Asap3PopupDebugWindow.argtypes = [TAsap3Hdl]
    Asap3PopupDebugWindow.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 749
if _libs["CANapAPI64.dll"].has("Asap3SaveDebugWindow", "stdcall"):
    Asap3SaveDebugWindow = _libs["CANapAPI64.dll"].get("Asap3SaveDebugWindow", "stdcall")
    Asap3SaveDebugWindow.argtypes = [TAsap3Hdl, String]
    Asap3SaveDebugWindow.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 750
if _libs["CANapAPI64.dll"].has("Asap3AttachAsap2", "stdcall"):
    Asap3AttachAsap2 = _libs["CANapAPI64.dll"].get("Asap3AttachAsap2", "stdcall")
    Asap3AttachAsap2.argtypes = [TAsap3Hdl, String, c_short, POINTER(TModulHdl)]
    Asap3AttachAsap2.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 751
if _libs["CANapAPI64.dll"].has("Asap3CreateModule", "stdcall"):
    Asap3CreateModule = _libs["CANapAPI64.dll"].get("Asap3CreateModule", "stdcall")
    Asap3CreateModule.argtypes = [TAsap3Hdl, String, String, c_short, c_short, POINTER(TModulHdl)]
    Asap3CreateModule.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 753
if _libs["CANapAPI64.dll"].has("Asap3CreateModule2", "stdcall"):
    Asap3CreateModule2 = _libs["CANapAPI64.dll"].get("Asap3CreateModule2", "stdcall")
    Asap3CreateModule2.argtypes = [TAsap3Hdl, String, String, c_short, c_short, c_bool, POINTER(TModulHdl)]
    Asap3CreateModule2.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 755
if _libs["CANapAPI64.dll"].has("Asap3CreateModule3", "stdcall"):
    Asap3CreateModule3 = _libs["CANapAPI64.dll"].get("Asap3CreateModule3", "stdcall")
    Asap3CreateModule3.argtypes = [TAsap3Hdl, String, String, c_short, c_short, c_bool, c_short, POINTER(TModulHdl)]
    Asap3CreateModule3.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 757
if _libs["CANapAPI64.dll"].has("Asap3CreateModule4", "stdcall"):
    Asap3CreateModule4 = _libs["CANapAPI64.dll"].get("Asap3CreateModule4", "stdcall")
    Asap3CreateModule4.argtypes = [TAsap3Hdl, String, String, c_short, c_short, String, c_bool, c_short, POINTER(TModulHdl)]
    Asap3CreateModule4.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 759
if _libs["CANapAPI64.dll"].has("Asap3CreateModuleSec", "stdcall"):
    Asap3CreateModuleSec = _libs["CANapAPI64.dll"].get("Asap3CreateModuleSec", "stdcall")
    Asap3CreateModuleSec.argtypes = [TAsap3Hdl, String, String, c_short, c_short, String, c_uint, String, c_bool, c_short, POINTER(TModulHdl)]
    Asap3CreateModuleSec.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 762
if _libs["CANapAPI64.dll"].has("Asap3GetModuleSecJobName", "stdcall"):
    Asap3GetModuleSecJobName = _libs["CANapAPI64.dll"].get("Asap3GetModuleSecJobName", "stdcall")
    Asap3GetModuleSecJobName.argtypes = [TAsap3Hdl, TModulHdl, String, POINTER(DWORD)]
    Asap3GetModuleSecJobName.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 763
if _libs["CANapAPI64.dll"].has("Asap3GetModuleCount", "stdcall"):
    Asap3GetModuleCount = _libs["CANapAPI64.dll"].get("Asap3GetModuleCount", "stdcall")
    Asap3GetModuleCount.argtypes = [TAsap3Hdl, POINTER(c_ulong)]
    Asap3GetModuleCount.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 764
if _libs["CANapAPI64.dll"].has("Asap3RestartMeasurementOnError", "stdcall"):
    Asap3RestartMeasurementOnError = _libs["CANapAPI64.dll"].get("Asap3RestartMeasurementOnError", "stdcall")
    Asap3RestartMeasurementOnError.argtypes = [TAsap3Hdl, TModulHdl, c_bool]
    Asap3RestartMeasurementOnError.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 765
if _libs["CANapAPI64.dll"].has("Asap3IsRestartMeasurementOnErrorEnabled", "stdcall"):
    Asap3IsRestartMeasurementOnErrorEnabled = _libs["CANapAPI64.dll"].get("Asap3IsRestartMeasurementOnErrorEnabled", "stdcall")
    Asap3IsRestartMeasurementOnErrorEnabled.argtypes = [TAsap3Hdl, TModulHdl, POINTER(c_bool)]
    Asap3IsRestartMeasurementOnErrorEnabled.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 766
if _libs["CANapAPI64.dll"].has("Asap3IsModuleActive", "stdcall"):
    Asap3IsModuleActive = _libs["CANapAPI64.dll"].get("Asap3IsModuleActive", "stdcall")
    Asap3IsModuleActive.argtypes = [TAsap3Hdl, TModulHdl, POINTER(c_bool)]
    Asap3IsModuleActive.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 767
if _libs["CANapAPI64.dll"].has("Asap3ModuleActivation", "stdcall"):
    Asap3ModuleActivation = _libs["CANapAPI64.dll"].get("Asap3ModuleActivation", "stdcall")
    Asap3ModuleActivation.argtypes = [TAsap3Hdl, TModulHdl, c_bool]
    Asap3ModuleActivation.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 768
if _libs["CANapAPI64.dll"].has("Asap3SwitchToMemoryPage", "stdcall"):
    Asap3SwitchToMemoryPage = _libs["CANapAPI64.dll"].get("Asap3SwitchToMemoryPage", "stdcall")
    Asap3SwitchToMemoryPage.argtypes = [TAsap3Hdl, TModulHdl, enum_e_RamMode]
    Asap3SwitchToMemoryPage.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 769
if _libs["CANapAPI64.dll"].has("Asap3GetMemoryPage", "stdcall"):
    Asap3GetMemoryPage = _libs["CANapAPI64.dll"].get("Asap3GetMemoryPage", "stdcall")
    Asap3GetMemoryPage.argtypes = [TAsap3Hdl, TModulHdl, POINTER(enum_e_RamMode)]
    Asap3GetMemoryPage.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 770
if _libs["CANapAPI64.dll"].has("Asap3GetDBObjectUnit", "stdcall"):
    Asap3GetDBObjectUnit = _libs["CANapAPI64.dll"].get("Asap3GetDBObjectUnit", "stdcall")
    Asap3GetDBObjectUnit.argtypes = [TAsap3Hdl, TModulHdl, String, String, POINTER(UINT)]
    Asap3GetDBObjectUnit.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 771
if _libs["CANapAPI64.dll"].has("Asap3GetDBObjectInfo", "stdcall"):
    Asap3GetDBObjectInfo = _libs["CANapAPI64.dll"].get("Asap3GetDBObjectInfo", "stdcall")
    Asap3GetDBObjectInfo.argtypes = [TAsap3Hdl, TModulHdl, String, POINTER(DBObjectInfo)]
    Asap3GetDBObjectInfo.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 772
if _libs["CANapAPI64.dll"].has("Asap3GetDatabaseObjects", "stdcall"):
    Asap3GetDatabaseObjects = _libs["CANapAPI64.dll"].get("Asap3GetDatabaseObjects", "stdcall")
    Asap3GetDatabaseObjects.argtypes = [TAsap3Hdl, TModulHdl, String, POINTER(UINT), TAsap3DBOType]
    Asap3GetDatabaseObjects.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 773
if _libs["CANapAPI64.dll"].has("Asap3GetDatabaseObjectsByType", "stdcall"):
    Asap3GetDatabaseObjectsByType = _libs["CANapAPI64.dll"].get("Asap3GetDatabaseObjectsByType", "stdcall")
    Asap3GetDatabaseObjectsByType.argtypes = [TAsap3Hdl, TModulHdl, String, POINTER(UINT), TAsap3DBOType, c_ulong]
    Asap3GetDatabaseObjectsByType.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 774
if _libs["CANapAPI64.dll"].has("Asap3GetAsap2", "stdcall"):
    Asap3GetAsap2 = _libs["CANapAPI64.dll"].get("Asap3GetAsap2", "stdcall")
    Asap3GetAsap2.argtypes = [TAsap3Hdl, TModulHdl, POINTER(POINTER(c_char))]
    Asap3GetAsap2.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 775
if _libs["CANapAPI64.dll"].has("Asap3GetDatabaseInfo", "stdcall"):
    Asap3GetDatabaseInfo = _libs["CANapAPI64.dll"].get("Asap3GetDatabaseInfo", "stdcall")
    Asap3GetDatabaseInfo.argtypes = [TAsap3Hdl, TModulHdl, POINTER(struct_DBFileInfo)]
    Asap3GetDatabaseInfo.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 776
if _libs["CANapAPI64.dll"].has("Asap3TransmitFile2ClientPc", "stdcall"):
    Asap3TransmitFile2ClientPc = _libs["CANapAPI64.dll"].get("Asap3TransmitFile2ClientPc", "stdcall")
    Asap3TransmitFile2ClientPc.argtypes = [TAsap3Hdl, String, String]
    Asap3TransmitFile2ClientPc.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 777
if _libs["CANapAPI64.dll"].has("Asap3GetModuleName", "stdcall"):
    Asap3GetModuleName = _libs["CANapAPI64.dll"].get("Asap3GetModuleName", "stdcall")
    Asap3GetModuleName.argtypes = [TAsap3Hdl, TModulHdl, POINTER(POINTER(c_char))]
    Asap3GetModuleName.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 778
if _libs["CANapAPI64.dll"].has("Asap3GetModuleHandle", "stdcall"):
    Asap3GetModuleHandle = _libs["CANapAPI64.dll"].get("Asap3GetModuleHandle", "stdcall")
    Asap3GetModuleHandle.argtypes = [TAsap3Hdl, String, POINTER(TModulHdl)]
    Asap3GetModuleHandle.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 779
if _libs["CANapAPI64.dll"].has("Asap3ReleaseModule", "stdcall"):
    Asap3ReleaseModule = _libs["CANapAPI64.dll"].get("Asap3ReleaseModule", "stdcall")
    Asap3ReleaseModule.argtypes = [TAsap3Hdl, TModulHdl]
    Asap3ReleaseModule.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 780
if _libs["CANapAPI64.dll"].has("Asap3GetCommunicationType", "stdcall"):
    Asap3GetCommunicationType = _libs["CANapAPI64.dll"].get("Asap3GetCommunicationType", "stdcall")
    Asap3GetCommunicationType.argtypes = [TAsap3Hdl, TModulHdl, POINTER(POINTER(c_char))]
    Asap3GetCommunicationType.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 781
if _libs["CANapAPI64.dll"].has("Asap3ECUOnOffline", "stdcall"):
    Asap3ECUOnOffline = _libs["CANapAPI64.dll"].get("Asap3ECUOnOffline", "stdcall")
    Asap3ECUOnOffline.argtypes = [TAsap3Hdl, TModulHdl, TAsap3ECUState, c_bool]
    Asap3ECUOnOffline.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 782
if _libs["CANapAPI64.dll"].has("Asap3IsECUOnline", "stdcall"):
    Asap3IsECUOnline = _libs["CANapAPI64.dll"].get("Asap3IsECUOnline", "stdcall")
    Asap3IsECUOnline.argtypes = [TAsap3Hdl, TModulHdl, POINTER(TAsap3ECUState)]
    Asap3IsECUOnline.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 783
if _libs["CANapAPI64.dll"].has("Asap3ReadByAddress", "stdcall"):
    Asap3ReadByAddress = _libs["CANapAPI64.dll"].get("Asap3ReadByAddress", "stdcall")
    Asap3ReadByAddress.argtypes = [TAsap3Hdl, TModulHdl, c_ulong, c_ubyte, c_ulong, POINTER(c_ubyte)]
    Asap3ReadByAddress.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 786
if _libs["CANapAPI64.dll"].has("Asap3WriteByAddress", "stdcall"):
    Asap3WriteByAddress = _libs["CANapAPI64.dll"].get("Asap3WriteByAddress", "stdcall")
    Asap3WriteByAddress.argtypes = [TAsap3Hdl, TModulHdl, c_ulong, c_ubyte, c_ulong, POINTER(c_ubyte)]
    Asap3WriteByAddress.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 789
if _libs["CANapAPI64.dll"].has("Asap3ReadCalibrationObject", "stdcall"):
    Asap3ReadCalibrationObject = _libs["CANapAPI64.dll"].get("Asap3ReadCalibrationObject", "stdcall")
    Asap3ReadCalibrationObject.argtypes = [TAsap3Hdl, TModulHdl, String, enum_TFormat, POINTER(TCalibrationObjectValue)]
    Asap3ReadCalibrationObject.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 792
if _libs["CANapAPI64.dll"].has("Asap3ReadCalibrationObject2", "stdcall"):
    Asap3ReadCalibrationObject2 = _libs["CANapAPI64.dll"].get("Asap3ReadCalibrationObject2", "stdcall")
    Asap3ReadCalibrationObject2.argtypes = [TAsap3Hdl, TModulHdl, String, enum_TFormat, c_bool, POINTER(TCalibrationObjectValue)]
    Asap3ReadCalibrationObject2.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 795
if _libs["CANapAPI64.dll"].has("Asap3ReadCalibrationObjectEx", "stdcall"):
    Asap3ReadCalibrationObjectEx = _libs["CANapAPI64.dll"].get("Asap3ReadCalibrationObjectEx", "stdcall")
    Asap3ReadCalibrationObjectEx.argtypes = [TAsap3Hdl, TModulHdl, String, enum_TFormat, POINTER(TCalibrationObjectValueEx)]
    Asap3ReadCalibrationObjectEx.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 798
if _libs["CANapAPI64.dll"].has("Asap3WriteCalibrationObject", "stdcall"):
    Asap3WriteCalibrationObject = _libs["CANapAPI64.dll"].get("Asap3WriteCalibrationObject", "stdcall")
    Asap3WriteCalibrationObject.argtypes = [TAsap3Hdl, TModulHdl, String, enum_TFormat, POINTER(TCalibrationObjectValue)]
    Asap3WriteCalibrationObject.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 801
if _libs["CANapAPI64.dll"].has("Asap3WriteCalibrationObjectEx", "stdcall"):
    Asap3WriteCalibrationObjectEx = _libs["CANapAPI64.dll"].get("Asap3WriteCalibrationObjectEx", "stdcall")
    Asap3WriteCalibrationObjectEx.argtypes = [TAsap3Hdl, TModulHdl, String, enum_TFormat, POINTER(TCalibrationObjectValueEx)]
    Asap3WriteCalibrationObjectEx.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 804
if _libs["CANapAPI64.dll"].has("Asap3TestObject", "stdcall"):
    Asap3TestObject = _libs["CANapAPI64.dll"].get("Asap3TestObject", "stdcall")
    Asap3TestObject.argtypes = [TAsap3Hdl, TModulHdl, String, POINTER(enum_TObjectType)]
    Asap3TestObject.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 806
if _libs["CANapAPI64.dll"].has("Asap3CalibrationObjectInfo", "stdcall"):
    Asap3CalibrationObjectInfo = _libs["CANapAPI64.dll"].get("Asap3CalibrationObjectInfo", "stdcall")
    Asap3CalibrationObjectInfo.argtypes = [TAsap3Hdl, TModulHdl, String, POINTER(c_short), POINTER(c_short)]
    Asap3CalibrationObjectInfo.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 809
if _libs["CANapAPI64.dll"].has("Asap3CalibrationObjectInfoEx", "stdcall"):
    Asap3CalibrationObjectInfoEx = _libs["CANapAPI64.dll"].get("Asap3CalibrationObjectInfoEx", "stdcall")
    Asap3CalibrationObjectInfoEx.argtypes = [TAsap3Hdl, TModulHdl, String, POINTER(c_short), POINTER(c_short), POINTER(enum_TValueType)]
    Asap3CalibrationObjectInfoEx.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 812
if _libs["CANapAPI64.dll"].has("Asap3CalibrationObjectRecordInfo", "stdcall"):
    Asap3CalibrationObjectRecordInfo = _libs["CANapAPI64.dll"].get("Asap3CalibrationObjectRecordInfo", "stdcall")
    Asap3CalibrationObjectRecordInfo.argtypes = [TAsap3Hdl, TModulHdl, String, POINTER(struct_TLayoutCoeffs), POINTER(c_short), POINTER(c_short)]
    Asap3CalibrationObjectRecordInfo.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 815
if _libs["CANapAPI64.dll"].has("Asap3GetEcuTasks", "stdcall"):
    Asap3GetEcuTasks = _libs["CANapAPI64.dll"].get("Asap3GetEcuTasks", "stdcall")
    Asap3GetEcuTasks.argtypes = [TAsap3Hdl, TModulHdl, POINTER(TTaskInfo), POINTER(c_ushort), c_ushort]
    Asap3GetEcuTasks.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 818
if _libs["CANapAPI64.dll"].has("Asap3GetEcuTasks2", "stdcall"):
    Asap3GetEcuTasks2 = _libs["CANapAPI64.dll"].get("Asap3GetEcuTasks2", "stdcall")
    Asap3GetEcuTasks2.argtypes = [TAsap3Hdl, TModulHdl, POINTER(TTaskInfo2), POINTER(c_ushort), c_ushort]
    Asap3GetEcuTasks2.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 821
if _libs["CANapAPI64.dll"].has("Asap3CreateLoggerConfiguration", "stdcall"):
    Asap3CreateLoggerConfiguration = _libs["CANapAPI64.dll"].get("Asap3CreateLoggerConfiguration", "stdcall")
    Asap3CreateLoggerConfiguration.argtypes = [TAsap3Hdl, TModulHdl]
    Asap3CreateLoggerConfiguration.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 822
if _libs["CANapAPI64.dll"].has("Asap3GetEcuDriverType", "stdcall"):
    Asap3GetEcuDriverType = _libs["CANapAPI64.dll"].get("Asap3GetEcuDriverType", "stdcall")
    Asap3GetEcuDriverType.argtypes = [TAsap3Hdl, TModulHdl, POINTER(tDriverType)]
    Asap3GetEcuDriverType.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 823
if _libs["CANapAPI64.dll"].has("Asap3HasResumeMode", "stdcall"):
    Asap3HasResumeMode = _libs["CANapAPI64.dll"].get("Asap3HasResumeMode", "stdcall")
    Asap3HasResumeMode.argtypes = [TAsap3Hdl, TModulHdl, POINTER(c_bool)]
    Asap3HasResumeMode.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 824
if _libs["CANapAPI64.dll"].has("Asap3SetResumeMode", "stdcall"):
    Asap3SetResumeMode = _libs["CANapAPI64.dll"].get("Asap3SetResumeMode", "stdcall")
    Asap3SetResumeMode.argtypes = [TAsap3Hdl, TModulHdl]
    Asap3SetResumeMode.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 825
if _libs["CANapAPI64.dll"].has("Asap3IsResumeModeActive", "stdcall"):
    Asap3IsResumeModeActive = _libs["CANapAPI64.dll"].get("Asap3IsResumeModeActive", "stdcall")
    Asap3IsResumeModeActive.argtypes = [TAsap3Hdl, TModulHdl, POINTER(c_bool)]
    Asap3IsResumeModeActive.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 826
if _libs["CANapAPI64.dll"].has("Asap3ClearResumeMode", "stdcall"):
    Asap3ClearResumeMode = _libs["CANapAPI64.dll"].get("Asap3ClearResumeMode", "stdcall")
    Asap3ClearResumeMode.argtypes = [TAsap3Hdl, TModulHdl]
    Asap3ClearResumeMode.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 827
if _libs["CANapAPI64.dll"].has("Asap3GetChnlDefaultRaster", "stdcall"):
    Asap3GetChnlDefaultRaster = _libs["CANapAPI64.dll"].get("Asap3GetChnlDefaultRaster", "stdcall")
    Asap3GetChnlDefaultRaster.argtypes = [TAsap3Hdl, TModulHdl, String, POINTER(c_ushort), POINTER(c_ushort)]
    Asap3GetChnlDefaultRaster.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 828
if _libs["CANapAPI64.dll"].has("Asap3SetupFifo", "stdcall"):
    Asap3SetupFifo = _libs["CANapAPI64.dll"].get("Asap3SetupFifo", "stdcall")
    Asap3SetupFifo.argtypes = [TAsap3Hdl, c_ushort, POINTER(tFifoSize)]
    Asap3SetupFifo.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 831
if _libs["CANapAPI64.dll"].has("Asap3SetupDataAcquisitionChnl", "stdcall"):
    Asap3SetupDataAcquisitionChnl = _libs["CANapAPI64.dll"].get("Asap3SetupDataAcquisitionChnl", "stdcall")
    Asap3SetupDataAcquisitionChnl.argtypes = [TAsap3Hdl, TModulHdl, String, enum_TFormat, c_ushort, c_ushort, c_bool]
    Asap3SetupDataAcquisitionChnl.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 835
if _libs["CANapAPI64.dll"].has("Asap3SetupDataAcquisitionChnl2", "stdcall"):
    Asap3SetupDataAcquisitionChnl2 = _libs["CANapAPI64.dll"].get("Asap3SetupDataAcquisitionChnl2", "stdcall")
    Asap3SetupDataAcquisitionChnl2.argtypes = [TAsap3Hdl, TModulHdl, String, enum_TFormat, c_ushort, c_ushort, c_bool, c_bool]
    Asap3SetupDataAcquisitionChnl2.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 839
if _libs["CANapAPI64.dll"].has("Asap3GetMeasurementListEntries", "stdcall"):
    Asap3GetMeasurementListEntries = _libs["CANapAPI64.dll"].get("Asap3GetMeasurementListEntries", "stdcall")
    Asap3GetMeasurementListEntries.argtypes = [TAsap3Hdl, TModulHdl, POINTER(POINTER(struct_MeasurementListEntries))]
    Asap3GetMeasurementListEntries.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 840
if _libs["CANapAPI64.dll"].has("Asap3GetMeasurementState", "stdcall"):
    Asap3GetMeasurementState = _libs["CANapAPI64.dll"].get("Asap3GetMeasurementState", "stdcall")
    Asap3GetMeasurementState.argtypes = [TAsap3Hdl, POINTER(tMeasurementState)]
    Asap3GetMeasurementState.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 841
if _libs["CANapAPI64.dll"].has("Asap3HasMCD3License", "stdcall"):
    Asap3HasMCD3License = _libs["CANapAPI64.dll"].get("Asap3HasMCD3License", "stdcall")
    Asap3HasMCD3License.argtypes = [TAsap3Hdl, POINTER(c_bool)]
    Asap3HasMCD3License.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 843
if _libs["CANapAPI64.dll"].has("Asap3GetRecorderType", "stdcall"):
    Asap3GetRecorderType = _libs["CANapAPI64.dll"].get("Asap3GetRecorderType", "stdcall")
    Asap3GetRecorderType.argtypes = [TAsap3Hdl, TRecorderID, POINTER(enum_TRecorderType)]
    Asap3GetRecorderType.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 844
if _libs["CANapAPI64.dll"].has("Asap3GetRecorderName", "stdcall"):
    Asap3GetRecorderName = _libs["CANapAPI64.dll"].get("Asap3GetRecorderName", "stdcall")
    Asap3GetRecorderName.argtypes = [TAsap3Hdl, TRecorderID, String, POINTER(c_long)]
    Asap3GetRecorderName.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 845
if _libs["CANapAPI64.dll"].has("Asap3GetRecorderCount", "stdcall"):
    Asap3GetRecorderCount = _libs["CANapAPI64.dll"].get("Asap3GetRecorderCount", "stdcall")
    Asap3GetRecorderCount.argtypes = [TAsap3Hdl, POINTER(c_ulong)]
    Asap3GetRecorderCount.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 846
if _libs["CANapAPI64.dll"].has("Asap3GetRecorderByIndex", "stdcall"):
    Asap3GetRecorderByIndex = _libs["CANapAPI64.dll"].get("Asap3GetRecorderByIndex", "stdcall")
    Asap3GetRecorderByIndex.argtypes = [TAsap3Hdl, c_ulong, POINTER(TRecorderID)]
    Asap3GetRecorderByIndex.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 847
if _libs["CANapAPI64.dll"].has("Asap3GetRecorderByName", "stdcall"):
    Asap3GetRecorderByName = _libs["CANapAPI64.dll"].get("Asap3GetRecorderByName", "stdcall")
    Asap3GetRecorderByName.argtypes = [TAsap3Hdl, String, POINTER(TRecorderID)]
    Asap3GetRecorderByName.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 848
if _libs["CANapAPI64.dll"].has("Asap3SelectRecorder", "stdcall"):
    Asap3SelectRecorder = _libs["CANapAPI64.dll"].get("Asap3SelectRecorder", "stdcall")
    Asap3SelectRecorder.argtypes = [TAsap3Hdl, TRecorderID]
    Asap3SelectRecorder.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 849
if _libs["CANapAPI64.dll"].has("Asap3GetSelectedRecorder", "stdcall"):
    Asap3GetSelectedRecorder = _libs["CANapAPI64.dll"].get("Asap3GetSelectedRecorder", "stdcall")
    Asap3GetSelectedRecorder.argtypes = [TAsap3Hdl, POINTER(TRecorderID)]
    Asap3GetSelectedRecorder.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 850
if _libs["CANapAPI64.dll"].has("Asap3RemoveRecorder", "stdcall"):
    Asap3RemoveRecorder = _libs["CANapAPI64.dll"].get("Asap3RemoveRecorder", "stdcall")
    Asap3RemoveRecorder.argtypes = [TAsap3Hdl, TRecorderID]
    Asap3RemoveRecorder.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 851
if _libs["CANapAPI64.dll"].has("Asap3EnableBusLoggingRecorderByModule", "stdcall"):
    Asap3EnableBusLoggingRecorderByModule = _libs["CANapAPI64.dll"].get("Asap3EnableBusLoggingRecorderByModule", "stdcall")
    Asap3EnableBusLoggingRecorderByModule.argtypes = [TAsap3Hdl, TRecorderID, TModulHdl, c_int]
    Asap3EnableBusLoggingRecorderByModule.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 852
if _libs["CANapAPI64.dll"].has("Asap3EnableBusLoggingRecorderByNetWork", "stdcall"):
    Asap3EnableBusLoggingRecorderByNetWork = _libs["CANapAPI64.dll"].get("Asap3EnableBusLoggingRecorderByNetWork", "stdcall")
    Asap3EnableBusLoggingRecorderByNetWork.argtypes = [TAsap3Hdl, TRecorderID, String, c_int]
    Asap3EnableBusLoggingRecorderByNetWork.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 853
if _libs["CANapAPI64.dll"].has("Asap3IsRecorderBusLoggingEnableByNetWork", "stdcall"):
    Asap3IsRecorderBusLoggingEnableByNetWork = _libs["CANapAPI64.dll"].get("Asap3IsRecorderBusLoggingEnableByNetWork", "stdcall")
    Asap3IsRecorderBusLoggingEnableByNetWork.argtypes = [TAsap3Hdl, TRecorderID, String, POINTER(c_int)]
    Asap3IsRecorderBusLoggingEnableByNetWork.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 854
if _libs["CANapAPI64.dll"].has("Asap3IsRecorderBusLoggingEnableByModule", "stdcall"):
    Asap3IsRecorderBusLoggingEnableByModule = _libs["CANapAPI64.dll"].get("Asap3IsRecorderBusLoggingEnableByModule", "stdcall")
    Asap3IsRecorderBusLoggingEnableByModule.argtypes = [TAsap3Hdl, TRecorderID, TModulHdl, POINTER(c_int)]
    Asap3IsRecorderBusLoggingEnableByModule.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 855
if _libs["CANapAPI64.dll"].has("Asap3GetRecorderMdfFileName", "stdcall"):
    Asap3GetRecorderMdfFileName = _libs["CANapAPI64.dll"].get("Asap3GetRecorderMdfFileName", "stdcall")
    Asap3GetRecorderMdfFileName.argtypes = [TAsap3Hdl, TRecorderID, String, POINTER(DWORD)]
    Asap3GetRecorderMdfFileName.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 856
if _libs["CANapAPI64.dll"].has("Asap3SetRecorderMdfFileName", "stdcall"):
    Asap3SetRecorderMdfFileName = _libs["CANapAPI64.dll"].get("Asap3SetRecorderMdfFileName", "stdcall")
    Asap3SetRecorderMdfFileName.argtypes = [TAsap3Hdl, TRecorderID, String]
    Asap3SetRecorderMdfFileName.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 857
if _libs["CANapAPI64.dll"].has("Asap3SetRecorderDataReduction", "stdcall"):
    Asap3SetRecorderDataReduction = _libs["CANapAPI64.dll"].get("Asap3SetRecorderDataReduction", "stdcall")
    Asap3SetRecorderDataReduction.argtypes = [TAsap3Hdl, TRecorderID, c_int]
    Asap3SetRecorderDataReduction.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 858
if _libs["CANapAPI64.dll"].has("Asap3GetRecorderDataReduction", "stdcall"):
    Asap3GetRecorderDataReduction = _libs["CANapAPI64.dll"].get("Asap3GetRecorderDataReduction", "stdcall")
    Asap3GetRecorderDataReduction.argtypes = [TAsap3Hdl, TRecorderID, POINTER(c_int)]
    Asap3GetRecorderDataReduction.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 859
if _libs["CANapAPI64.dll"].has("Asap3GetRecorderState", "stdcall"):
    Asap3GetRecorderState = _libs["CANapAPI64.dll"].get("Asap3GetRecorderState", "stdcall")
    Asap3GetRecorderState.argtypes = [TAsap3Hdl, TRecorderID, POINTER(enum_EnRecorderState)]
    Asap3GetRecorderState.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 860
if _libs["CANapAPI64.dll"].has("Asap3PauseRecorder", "stdcall"):
    Asap3PauseRecorder = _libs["CANapAPI64.dll"].get("Asap3PauseRecorder", "stdcall")
    Asap3PauseRecorder.argtypes = [TAsap3Hdl, TRecorderID, c_bool]
    Asap3PauseRecorder.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 861
if _libs["CANapAPI64.dll"].has("Asap3StartRecorder", "stdcall"):
    Asap3StartRecorder = _libs["CANapAPI64.dll"].get("Asap3StartRecorder", "stdcall")
    Asap3StartRecorder.argtypes = [TAsap3Hdl, TRecorderID]
    Asap3StartRecorder.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 862
if _libs["CANapAPI64.dll"].has("Asap3StopRecorder", "stdcall"):
    Asap3StopRecorder = _libs["CANapAPI64.dll"].get("Asap3StopRecorder", "stdcall")
    Asap3StopRecorder.argtypes = [TAsap3Hdl, TRecorderID, c_bool]
    Asap3StopRecorder.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 863
if _libs["CANapAPI64.dll"].has("Asap3EnableRecorder", "stdcall"):
    Asap3EnableRecorder = _libs["CANapAPI64.dll"].get("Asap3EnableRecorder", "stdcall")
    Asap3EnableRecorder.argtypes = [TAsap3Hdl, TRecorderID, c_bool]
    Asap3EnableRecorder.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 864
if _libs["CANapAPI64.dll"].has("Asap3IsRecorderEnabled", "stdcall"):
    Asap3IsRecorderEnabled = _libs["CANapAPI64.dll"].get("Asap3IsRecorderEnabled", "stdcall")
    Asap3IsRecorderEnabled.argtypes = [TAsap3Hdl, TRecorderID, POINTER(c_bool)]
    Asap3IsRecorderEnabled.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 865
if _libs["CANapAPI64.dll"].has("Asap3ResetDataAcquisitionChnlsByModule", "stdcall"):
    Asap3ResetDataAcquisitionChnlsByModule = _libs["CANapAPI64.dll"].get("Asap3ResetDataAcquisitionChnlsByModule", "stdcall")
    Asap3ResetDataAcquisitionChnlsByModule.argtypes = [TAsap3Hdl, TModulHdl]
    Asap3ResetDataAcquisitionChnlsByModule.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 866
if _libs["CANapAPI64.dll"].has("Asap3ResetDataAcquisitionChnls", "stdcall"):
    Asap3ResetDataAcquisitionChnls = _libs["CANapAPI64.dll"].get("Asap3ResetDataAcquisitionChnls", "stdcall")
    Asap3ResetDataAcquisitionChnls.argtypes = [TAsap3Hdl]
    Asap3ResetDataAcquisitionChnls.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 867
if _libs["CANapAPI64.dll"].has("Asap3TimeSync", "stdcall"):
    Asap3TimeSync = _libs["CANapAPI64.dll"].get("Asap3TimeSync", "stdcall")
    Asap3TimeSync.argtypes = [TAsap3Hdl, c_bool]
    Asap3TimeSync.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 868
if _libs["CANapAPI64.dll"].has("Asap3IsTimeSyncEnabled", "stdcall"):
    Asap3IsTimeSyncEnabled = _libs["CANapAPI64.dll"].get("Asap3IsTimeSyncEnabled", "stdcall")
    Asap3IsTimeSyncEnabled.argtypes = [TAsap3Hdl, POINTER(c_bool)]
    Asap3IsTimeSyncEnabled.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 869
if _libs["CANapAPI64.dll"].has("Asap3StartDataAcquisition", "stdcall"):
    Asap3StartDataAcquisition = _libs["CANapAPI64.dll"].get("Asap3StartDataAcquisition", "stdcall")
    Asap3StartDataAcquisition.argtypes = [TAsap3Hdl]
    Asap3StartDataAcquisition.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 870
if _libs["CANapAPI64.dll"].has("Asap3ConnectDataAcquisition", "stdcall"):
    Asap3ConnectDataAcquisition = _libs["CANapAPI64.dll"].get("Asap3ConnectDataAcquisition", "stdcall")
    Asap3ConnectDataAcquisition.argtypes = [TAsap3Hdl]
    Asap3ConnectDataAcquisition.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 871
if _libs["CANapAPI64.dll"].has("Asap3StartResumedDataAcquisition", "stdcall"):
    Asap3StartResumedDataAcquisition = _libs["CANapAPI64.dll"].get("Asap3StartResumedDataAcquisition", "stdcall")
    Asap3StartResumedDataAcquisition.argtypes = [TAsap3Hdl]
    Asap3StartResumedDataAcquisition.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 872
if _libs["CANapAPI64.dll"].has("Asap3StopDataAcquisition", "stdcall"):
    Asap3StopDataAcquisition = _libs["CANapAPI64.dll"].get("Asap3StopDataAcquisition", "stdcall")
    Asap3StopDataAcquisition.argtypes = [TAsap3Hdl]
    Asap3StopDataAcquisition.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 873
if _libs["CANapAPI64.dll"].has("Asap3DisconnectDataAcquisition", "stdcall"):
    Asap3DisconnectDataAcquisition = _libs["CANapAPI64.dll"].get("Asap3DisconnectDataAcquisition", "stdcall")
    Asap3DisconnectDataAcquisition.argtypes = [TAsap3Hdl]
    Asap3DisconnectDataAcquisition.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 874
if _libs["CANapAPI64.dll"].has("Asap3GetFifoLevel", "stdcall"):
    Asap3GetFifoLevel = _libs["CANapAPI64.dll"].get("Asap3GetFifoLevel", "stdcall")
    Asap3GetFifoLevel.argtypes = [TAsap3Hdl, TModulHdl, c_ushort]
    Asap3GetFifoLevel.restype = c_long

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 875
if _libs["CANapAPI64.dll"].has("Asap3CheckOverrun", "stdcall"):
    Asap3CheckOverrun = _libs["CANapAPI64.dll"].get("Asap3CheckOverrun", "stdcall")
    Asap3CheckOverrun.argtypes = [TAsap3Hdl, TModulHdl, c_ushort, c_bool]
    Asap3CheckOverrun.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 876
if _libs["CANapAPI64.dll"].has("Asap3GetNextSample", "stdcall"):
    Asap3GetNextSample = _libs["CANapAPI64.dll"].get("Asap3GetNextSample", "stdcall")
    Asap3GetNextSample.argtypes = [TAsap3Hdl, TModulHdl, c_ushort, POINTER(TTime), POINTER(POINTER(c_double))]
    Asap3GetNextSample.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 883
if _libs["CANapAPI64.dll"].has("Asap3GetCurrentValues", "stdcall"):
    Asap3GetCurrentValues = _libs["CANapAPI64.dll"].get("Asap3GetCurrentValues", "stdcall")
    Asap3GetCurrentValues.argtypes = [TAsap3Hdl, TModulHdl, c_ushort, POINTER(TTime), POINTER(c_double), c_ushort]
    Asap3GetCurrentValues.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 892
if _libs["CANapAPI64.dll"].has("Asap3GetNextSampleBlock", "stdcall"):
    Asap3GetNextSampleBlock = _libs["CANapAPI64.dll"].get("Asap3GetNextSampleBlock", "stdcall")
    Asap3GetNextSampleBlock.argtypes = [TAsap3Hdl, TModulHdl, c_ushort, c_long, POINTER(POINTER(struct_tSampleBlockObject))]
    Asap3GetNextSampleBlock.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 897
if _libs["CANapAPI64.dll"].has("Asap3UseNAN", "stdcall"):
    Asap3UseNAN = _libs["CANapAPI64.dll"].get("Asap3UseNAN", "stdcall")
    Asap3UseNAN.argtypes = [TAsap3Hdl, c_bool]
    Asap3UseNAN.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 898
if _libs["CANapAPI64.dll"].has("Asap3IsNANUsed", "stdcall"):
    Asap3IsNANUsed = _libs["CANapAPI64.dll"].get("Asap3IsNANUsed", "stdcall")
    Asap3IsNANUsed.argtypes = [TAsap3Hdl, POINTER(c_bool)]
    Asap3IsNANUsed.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 899
if _libs["CANapAPI64.dll"].has("Asap3SetMdfFilename", "stdcall"):
    Asap3SetMdfFilename = _libs["CANapAPI64.dll"].get("Asap3SetMdfFilename", "stdcall")
    Asap3SetMdfFilename.argtypes = [TAsap3Hdl, String]
    Asap3SetMdfFilename.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 900
if _libs["CANapAPI64.dll"].has("Asap3GetMdfFilename", "stdcall"):
    Asap3GetMdfFilename = _libs["CANapAPI64.dll"].get("Asap3GetMdfFilename", "stdcall")
    Asap3GetMdfFilename.argtypes = [TAsap3Hdl, POINTER(POINTER(c_char))]
    Asap3GetMdfFilename.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 902
if _libs["CANapAPI64.dll"].has("Asap3MatlabConversion", "stdcall"):
    Asap3MatlabConversion = _libs["CANapAPI64.dll"].get("Asap3MatlabConversion", "stdcall")
    Asap3MatlabConversion.argtypes = [TAsap3Hdl, String, String]
    Asap3MatlabConversion.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 903
if _libs["CANapAPI64.dll"].has("Asap3MatlabConversionAsync", "stdcall"):
    Asap3MatlabConversionAsync = _libs["CANapAPI64.dll"].get("Asap3MatlabConversionAsync", "stdcall")
    Asap3MatlabConversionAsync.argtypes = [TAsap3Hdl, String, String]
    Asap3MatlabConversionAsync.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 904
if _libs["CANapAPI64.dll"].has("Asap3MDFConverterCount", "stdcall"):
    Asap3MDFConverterCount = _libs["CANapAPI64.dll"].get("Asap3MDFConverterCount", "stdcall")
    Asap3MDFConverterCount.argtypes = [TAsap3Hdl, POINTER(c_int)]
    Asap3MDFConverterCount.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 905
if _libs["CANapAPI64.dll"].has("Asap3MDFConvert", "stdcall"):
    Asap3MDFConvert = _libs["CANapAPI64.dll"].get("Asap3MDFConvert", "stdcall")
    Asap3MDFConvert.argtypes = [TAsap3Hdl, String, String, String, c_bool]
    Asap3MDFConvert.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 906
if _libs["CANapAPI64.dll"].has("Asap3MDFConverterInfo", "stdcall"):
    Asap3MDFConverterInfo = _libs["CANapAPI64.dll"].get("Asap3MDFConverterInfo", "stdcall")
    Asap3MDFConverterInfo.argtypes = [TAsap3Hdl, c_int, POINTER(struct_TConverterInfo)]
    Asap3MDFConverterInfo.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 907
if _libs["CANapAPI64.dll"].has("Asap3GetNetworkName", "stdcall"):
    Asap3GetNetworkName = _libs["CANapAPI64.dll"].get("Asap3GetNetworkName", "stdcall")
    Asap3GetNetworkName.argtypes = [TAsap3Hdl, TModulHdl, String, POINTER(c_uint)]
    Asap3GetNetworkName.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 908
if _libs["CANapAPI64.dll"].has("Asap3GetNetworkDevices", "stdcall"):
    Asap3GetNetworkDevices = _libs["CANapAPI64.dll"].get("Asap3GetNetworkDevices", "stdcall")
    Asap3GetNetworkDevices.argtypes = [TAsap3Hdl, String, POINTER(TModulHdl), POINTER(c_uint)]
    Asap3GetNetworkDevices.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 909
if _libs["CANapAPI64.dll"].has("Asap3ActivateNetwork", "stdcall"):
    Asap3ActivateNetwork = _libs["CANapAPI64.dll"].get("Asap3ActivateNetwork", "stdcall")
    Asap3ActivateNetwork.argtypes = [TAsap3Hdl, String, c_bool]
    Asap3ActivateNetwork.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 910
if _libs["CANapAPI64.dll"].has("Asap3IsNetworkActivated", "stdcall"):
    Asap3IsNetworkActivated = _libs["CANapAPI64.dll"].get("Asap3IsNetworkActivated", "stdcall")
    Asap3IsNetworkActivated.argtypes = [TAsap3Hdl, String, POINTER(c_bool)]
    Asap3IsNetworkActivated.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 911
if _libs["CANapAPI64.dll"].has("Asap3GetSecProfileCount", "stdcall"):
    Asap3GetSecProfileCount = _libs["CANapAPI64.dll"].get("Asap3GetSecProfileCount", "stdcall")
    Asap3GetSecProfileCount.argtypes = [TAsap3Hdl, POINTER(c_uint)]
    Asap3GetSecProfileCount.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 912
if _libs["CANapAPI64.dll"].has("Asap3GetSecProfileIdentifier", "stdcall"):
    Asap3GetSecProfileIdentifier = _libs["CANapAPI64.dll"].get("Asap3GetSecProfileIdentifier", "stdcall")
    Asap3GetSecProfileIdentifier.argtypes = [TAsap3Hdl, String, POINTER(DWORD)]
    Asap3GetSecProfileIdentifier.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 913
if _libs["CANapAPI64.dll"].has("Asap3GetSecProfileInfo", "stdcall"):
    Asap3GetSecProfileInfo = _libs["CANapAPI64.dll"].get("Asap3GetSecProfileInfo", "stdcall")
    Asap3GetSecProfileInfo.argtypes = [TAsap3Hdl, c_uint, POINTER(struct_SecProfileEntry)]
    Asap3GetSecProfileInfo.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 914
if _libs["CANapAPI64.dll"].has("Asap3AddSecProfileToNetwork", "stdcall"):
    Asap3AddSecProfileToNetwork = _libs["CANapAPI64.dll"].get("Asap3AddSecProfileToNetwork", "stdcall")
    Asap3AddSecProfileToNetwork.argtypes = [TAsap3Hdl, c_uint, String]
    Asap3AddSecProfileToNetwork.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 915
if _libs["CANapAPI64.dll"].has("Asap3_CCP_Request", "stdcall"):
    Asap3_CCP_Request = _libs["CANapAPI64.dll"].get("Asap3_CCP_Request", "stdcall")
    Asap3_CCP_Request.argtypes = [TAsap3Hdl, TModulHdl, POINTER(c_ubyte), c_ulong, c_ulong, POINTER(c_ubyte), c_ulong, POINTER(c_ulong)]
    Asap3_CCP_Request.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 923
if _libs["CANapAPI64.dll"].has("Asap3ExecuteScript", "stdcall"):
    Asap3ExecuteScript = _libs["CANapAPI64.dll"].get("Asap3ExecuteScript", "stdcall")
    Asap3ExecuteScript.argtypes = [TAsap3Hdl, TModulHdl, c_bool, String]
    Asap3ExecuteScript.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 927
if _libs["CANapAPI64.dll"].has("Asap3SelectObjects", "stdcall"):
    Asap3SelectObjects = _libs["CANapAPI64.dll"].get("Asap3SelectObjects", "stdcall")
    Asap3SelectObjects.argtypes = [TAsap3Hdl, TModulHdl, enum_TObjectType, String]
    Asap3SelectObjects.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 929
if _libs["CANapAPI64.dll"].has("Asap3RestoreWndSize", "stdcall"):
    Asap3RestoreWndSize = _libs["CANapAPI64.dll"].get("Asap3RestoreWndSize", "stdcall")
    Asap3RestoreWndSize.argtypes = [TAsap3Hdl]
    Asap3RestoreWndSize.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 930
if _libs["CANapAPI64.dll"].has("Asap3RestoreWndSize2", "stdcall"):
    Asap3RestoreWndSize2 = _libs["CANapAPI64.dll"].get("Asap3RestoreWndSize2", "stdcall")
    Asap3RestoreWndSize2.argtypes = [TAsap3Hdl, c_long]
    Asap3RestoreWndSize2.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 931
if _libs["CANapAPI64.dll"].has("Asap3CopyBinaryFile", "stdcall"):
    Asap3CopyBinaryFile = _libs["CANapAPI64.dll"].get("Asap3CopyBinaryFile", "stdcall")
    Asap3CopyBinaryFile.argtypes = [TAsap3Hdl, TModulHdl, TAsap3FileType, TAsap3FileType, String]
    Asap3CopyBinaryFile.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 932
if _libs["CANapAPI64.dll"].has("Asap3ReadObjectParameter", "stdcall"):
    Asap3ReadObjectParameter = _libs["CANapAPI64.dll"].get("Asap3ReadObjectParameter", "stdcall")
    Asap3ReadObjectParameter.argtypes = [TAsap3Hdl, TModulHdl, String, enum_TFormat, POINTER(TAsap3DataType), POINTER(c_ulong), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    Asap3ReadObjectParameter.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 933
if _libs["CANapAPI64.dll"].has("Asap3ExecuteScriptEx", "stdcall"):
    Asap3ExecuteScriptEx = _libs["CANapAPI64.dll"].get("Asap3ExecuteScriptEx", "stdcall")
    Asap3ExecuteScriptEx.argtypes = [TAsap3Hdl, TModulHdl, c_bool, String, POINTER(TScriptHdl)]
    Asap3ExecuteScriptEx.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 938
if _libs["CANapAPI64.dll"].has("Asap3GetScriptState", "stdcall"):
    Asap3GetScriptState = _libs["CANapAPI64.dll"].get("Asap3GetScriptState", "stdcall")
    Asap3GetScriptState.argtypes = [TAsap3Hdl, TScriptHdl, POINTER(enum_TScriptStatus), String, POINTER(DWORD)]
    Asap3GetScriptState.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 939
if _libs["CANapAPI64.dll"].has("Asap3StopScript", "stdcall"):
    Asap3StopScript = _libs["CANapAPI64.dll"].get("Asap3StopScript", "stdcall")
    Asap3StopScript.argtypes = [TAsap3Hdl, TScriptHdl]
    Asap3StopScript.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 941
if _libs["CANapAPI64.dll"].has("Asap3GetScriptResultValue", "stdcall"):
    Asap3GetScriptResultValue = _libs["CANapAPI64.dll"].get("Asap3GetScriptResultValue", "stdcall")
    Asap3GetScriptResultValue.argtypes = [TAsap3Hdl, TScriptHdl, POINTER(c_double)]
    Asap3GetScriptResultValue.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 942
if _libs["CANapAPI64.dll"].has("Asap3GetScriptResultString", "stdcall"):
    Asap3GetScriptResultString = _libs["CANapAPI64.dll"].get("Asap3GetScriptResultString", "stdcall")
    Asap3GetScriptResultString.argtypes = [TAsap3Hdl, TScriptHdl, String, POINTER(DWORD)]
    Asap3GetScriptResultString.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 943
if _libs["CANapAPI64.dll"].has("Asap3ReleaseScript", "stdcall"):
    Asap3ReleaseScript = _libs["CANapAPI64.dll"].get("Asap3ReleaseScript", "stdcall")
    Asap3ReleaseScript.argtypes = [TAsap3Hdl, TScriptHdl]
    Asap3ReleaseScript.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 944
if _libs["CANapAPI64.dll"].has("Asap3DiagEnableTesterPresent", "stdcall"):
    Asap3DiagEnableTesterPresent = _libs["CANapAPI64.dll"].get("Asap3DiagEnableTesterPresent", "stdcall")
    Asap3DiagEnableTesterPresent.argtypes = [TAsap3Hdl, TModulHdl, c_bool]
    Asap3DiagEnableTesterPresent.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 945
if _libs["CANapAPI64.dll"].has("Asap3DiagIsTesterPresentEnabled", "stdcall"):
    Asap3DiagIsTesterPresentEnabled = _libs["CANapAPI64.dll"].get("Asap3DiagIsTesterPresentEnabled", "stdcall")
    Asap3DiagIsTesterPresentEnabled.argtypes = [TAsap3Hdl, TModulHdl, POINTER(c_bool)]
    Asap3DiagIsTesterPresentEnabled.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 946
if _libs["CANapAPI64.dll"].has("Asap3DiagExecuteJob", "stdcall"):
    Asap3DiagExecuteJob = _libs["CANapAPI64.dll"].get("Asap3DiagExecuteJob", "stdcall")
    Asap3DiagExecuteJob.argtypes = [TAsap3Hdl, TModulHdl, String, String, c_bool, POINTER(POINTER(struct_DiagJobResponse))]
    Asap3DiagExecuteJob.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 947
if _libs["CANapAPI64.dll"].has("Asap3DiagCreateRawRequest", "stdcall"):
    Asap3DiagCreateRawRequest = _libs["CANapAPI64.dll"].get("Asap3DiagCreateRawRequest", "stdcall")
    Asap3DiagCreateRawRequest.argtypes = [TAsap3Hdl, TModulHdl, POINTER(c_ubyte), c_uint, POINTER(TAsap3DiagHdl)]
    Asap3DiagCreateRawRequest.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 948
if _libs["CANapAPI64.dll"].has("Asap3DiagCreateRawRequest2", "stdcall"):
    Asap3DiagCreateRawRequest2 = _libs["CANapAPI64.dll"].get("Asap3DiagCreateRawRequest2", "stdcall")
    Asap3DiagCreateRawRequest2.argtypes = [TAsap3Hdl, TModulHdl, POINTER(c_ubyte), c_uint, POINTER(TAsap3DiagHdl)]
    Asap3DiagCreateRawRequest2.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 949
if _libs["CANapAPI64.dll"].has("Asap3DiagCreateSymbolicRequest", "stdcall"):
    Asap3DiagCreateSymbolicRequest = _libs["CANapAPI64.dll"].get("Asap3DiagCreateSymbolicRequest", "stdcall")
    Asap3DiagCreateSymbolicRequest.argtypes = [TAsap3Hdl, TModulHdl, String, POINTER(TAsap3DiagHdl)]
    Asap3DiagCreateSymbolicRequest.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 951
if _libs["CANapAPI64.dll"].has("Asap3DiagExecute", "stdcall"):
    Asap3DiagExecute = _libs["CANapAPI64.dll"].get("Asap3DiagExecute", "stdcall")
    Asap3DiagExecute.argtypes = [TAsap3Hdl, TAsap3DiagHdl, c_int]
    Asap3DiagExecute.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 952
if _libs["CANapAPI64.dll"].has("Asap3DiagGetServiceState", "stdcall"):
    Asap3DiagGetServiceState = _libs["CANapAPI64.dll"].get("Asap3DiagGetServiceState", "stdcall")
    Asap3DiagGetServiceState.argtypes = [TAsap3Hdl, TAsap3DiagHdl, POINTER(enum_eServiceStates)]
    Asap3DiagGetServiceState.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 953
if _libs["CANapAPI64.dll"].has("Asap3DiagReleaseService", "stdcall"):
    Asap3DiagReleaseService = _libs["CANapAPI64.dll"].get("Asap3DiagReleaseService", "stdcall")
    Asap3DiagReleaseService.argtypes = [TAsap3Hdl, TAsap3DiagHdl]
    Asap3DiagReleaseService.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 954
if _libs["CANapAPI64.dll"].has("Asap3DiagSetStringParameter", "stdcall"):
    Asap3DiagSetStringParameter = _libs["CANapAPI64.dll"].get("Asap3DiagSetStringParameter", "stdcall")
    Asap3DiagSetStringParameter.argtypes = [TAsap3Hdl, TAsap3DiagHdl, String, String]
    Asap3DiagSetStringParameter.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 955
if _libs["CANapAPI64.dll"].has("Asap3DiagSetRawParameter", "stdcall"):
    Asap3DiagSetRawParameter = _libs["CANapAPI64.dll"].get("Asap3DiagSetRawParameter", "stdcall")
    Asap3DiagSetRawParameter.argtypes = [TAsap3Hdl, TAsap3DiagHdl, String, POINTER(c_ubyte), DWORD]
    Asap3DiagSetRawParameter.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 956
if _libs["CANapAPI64.dll"].has("Asap3DiagSetNumericParameter", "stdcall"):
    Asap3DiagSetNumericParameter = _libs["CANapAPI64.dll"].get("Asap3DiagSetNumericParameter", "stdcall")
    Asap3DiagSetNumericParameter.argtypes = [TAsap3Hdl, TAsap3DiagHdl, String, POINTER(struct_DiagNumericParameter)]
    Asap3DiagSetNumericParameter.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 957
if _libs["CANapAPI64.dll"].has("Asap3DiagGetResponseCount", "stdcall"):
    Asap3DiagGetResponseCount = _libs["CANapAPI64.dll"].get("Asap3DiagGetResponseCount", "stdcall")
    Asap3DiagGetResponseCount.argtypes = [TAsap3Hdl, TAsap3DiagHdl, POINTER(c_uint)]
    Asap3DiagGetResponseCount.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 958
if _libs["CANapAPI64.dll"].has("Asap3DiagIsPositiveResponse", "stdcall"):
    Asap3DiagIsPositiveResponse = _libs["CANapAPI64.dll"].get("Asap3DiagIsPositiveResponse", "stdcall")
    Asap3DiagIsPositiveResponse.argtypes = [TAsap3Hdl, TAsap3DiagHdl, c_long, POINTER(c_int)]
    Asap3DiagIsPositiveResponse.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 959
if _libs["CANapAPI64.dll"].has("Asap3DiagGetResponseStream", "stdcall"):
    Asap3DiagGetResponseStream = _libs["CANapAPI64.dll"].get("Asap3DiagGetResponseStream", "stdcall")
    Asap3DiagGetResponseStream.argtypes = [TAsap3Hdl, TAsap3DiagHdl, POINTER(c_ubyte), POINTER(DWORD), c_long]
    Asap3DiagGetResponseStream.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 960
if _libs["CANapAPI64.dll"].has("Asap3DiagGetStringResponseParameter", "stdcall"):
    Asap3DiagGetStringResponseParameter = _libs["CANapAPI64.dll"].get("Asap3DiagGetStringResponseParameter", "stdcall")
    Asap3DiagGetStringResponseParameter.argtypes = [TAsap3Hdl, TAsap3DiagHdl, String, c_long, String, POINTER(DWORD)]
    Asap3DiagGetStringResponseParameter.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 961
if _libs["CANapAPI64.dll"].has("Asap3DiagGetRawResponseParameter", "stdcall"):
    Asap3DiagGetRawResponseParameter = _libs["CANapAPI64.dll"].get("Asap3DiagGetRawResponseParameter", "stdcall")
    Asap3DiagGetRawResponseParameter.argtypes = [TAsap3Hdl, TAsap3DiagHdl, String, c_long, POINTER(c_ubyte), POINTER(DWORD)]
    Asap3DiagGetRawResponseParameter.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 962
if _libs["CANapAPI64.dll"].has("Asap3DiagGetNumericResponseParameter", "stdcall"):
    Asap3DiagGetNumericResponseParameter = _libs["CANapAPI64.dll"].get("Asap3DiagGetNumericResponseParameter", "stdcall")
    Asap3DiagGetNumericResponseParameter.argtypes = [TAsap3Hdl, TAsap3DiagHdl, String, c_long, POINTER(struct_DiagNumericParameter)]
    Asap3DiagGetNumericResponseParameter.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 963
if _libs["CANapAPI64.dll"].has("Asap3DiagIsComplexResponseParameter", "stdcall"):
    Asap3DiagIsComplexResponseParameter = _libs["CANapAPI64.dll"].get("Asap3DiagIsComplexResponseParameter", "stdcall")
    Asap3DiagIsComplexResponseParameter.argtypes = [TAsap3Hdl, TAsap3DiagHdl, String, c_long, POINTER(c_int)]
    Asap3DiagIsComplexResponseParameter.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 964
if _libs["CANapAPI64.dll"].has("Asap3DiagGetComplexNumericResponseParameter", "stdcall"):
    Asap3DiagGetComplexNumericResponseParameter = _libs["CANapAPI64.dll"].get("Asap3DiagGetComplexNumericResponseParameter", "stdcall")
    Asap3DiagGetComplexNumericResponseParameter.argtypes = [TAsap3Hdl, TAsap3DiagHdl, String, c_long, String, c_ulong, POINTER(struct_DiagNumericParameter)]
    Asap3DiagGetComplexNumericResponseParameter.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 965
if _libs["CANapAPI64.dll"].has("Asap3DiagGetComplexStringResponseParameter", "stdcall"):
    Asap3DiagGetComplexStringResponseParameter = _libs["CANapAPI64.dll"].get("Asap3DiagGetComplexStringResponseParameter", "stdcall")
    Asap3DiagGetComplexStringResponseParameter.argtypes = [TAsap3Hdl, TAsap3DiagHdl, String, c_long, String, c_ulong, String, POINTER(DWORD)]
    Asap3DiagGetComplexStringResponseParameter.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 966
if _libs["CANapAPI64.dll"].has("Asap3DiagGetComplexRawResponseParameter", "stdcall"):
    Asap3DiagGetComplexRawResponseParameter = _libs["CANapAPI64.dll"].get("Asap3DiagGetComplexRawResponseParameter", "stdcall")
    Asap3DiagGetComplexRawResponseParameter.argtypes = [TAsap3Hdl, TAsap3DiagHdl, String, c_long, String, c_ulong, String, POINTER(DWORD)]
    Asap3DiagGetComplexRawResponseParameter.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 967
if _libs["CANapAPI64.dll"].has("Asap3DiagGetResponseCode", "stdcall"):
    Asap3DiagGetResponseCode = _libs["CANapAPI64.dll"].get("Asap3DiagGetResponseCode", "stdcall")
    Asap3DiagGetResponseCode.argtypes = [TAsap3Hdl, TAsap3DiagHdl, c_long, POINTER(c_ubyte)]
    Asap3DiagGetResponseCode.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 968
if _libs["CANapAPI64.dll"].has("Asap3DiagGetComplexIterationCount", "stdcall"):
    Asap3DiagGetComplexIterationCount = _libs["CANapAPI64.dll"].get("Asap3DiagGetComplexIterationCount", "stdcall")
    Asap3DiagGetComplexIterationCount.argtypes = [TAsap3Hdl, TAsap3DiagHdl, String, c_long, POINTER(c_ulong)]
    Asap3DiagGetComplexIterationCount.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 969
if _libs["CANapAPI64.dll"].has("Asap3LoadCNAFile", "stdcall"):
    Asap3LoadCNAFile = _libs["CANapAPI64.dll"].get("Asap3LoadCNAFile", "stdcall")
    Asap3LoadCNAFile.argtypes = [TAsap3Hdl, String]
    Asap3LoadCNAFile.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 970
if _libs["CANapAPI64.dll"].has("Asap3GetCNAFilename", "stdcall"):
    Asap3GetCNAFilename = _libs["CANapAPI64.dll"].get("Asap3GetCNAFilename", "stdcall")
    Asap3GetCNAFilename.argtypes = [TAsap3Hdl, String, POINTER(c_uint)]
    Asap3GetCNAFilename.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 973
if _libs["CANapAPI64.dll"].has("Asap3GetCanapeModuleParam", "stdcall"):
    Asap3GetCanapeModuleParam = _libs["CANapAPI64.dll"].get("Asap3GetCanapeModuleParam", "stdcall")
    Asap3GetCanapeModuleParam.argtypes = [TAsap3Hdl, TModulHdl, String, String, POINTER(c_uint)]
    Asap3GetCanapeModuleParam.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 975
if _libs["CANapAPI64.dll"].has("Asap3SetCanapeModuleParam", "stdcall"):
    Asap3SetCanapeModuleParam = _libs["CANapAPI64.dll"].get("Asap3SetCanapeModuleParam", "stdcall")
    Asap3SetCanapeModuleParam.argtypes = [TAsap3Hdl, TModulHdl, String, String]
    Asap3SetCanapeModuleParam.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 978
if _libs["CANapAPI64.dll"].has("Asap3GetCanapeProjectParam", "stdcall"):
    Asap3GetCanapeProjectParam = _libs["CANapAPI64.dll"].get("Asap3GetCanapeProjectParam", "stdcall")
    Asap3GetCanapeProjectParam.argtypes = [TAsap3Hdl, String, String, String, POINTER(c_uint)]
    Asap3GetCanapeProjectParam.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 979
if _libs["CANapAPI64.dll"].has("Asap3SetCanapeProjectParam", "stdcall"):
    Asap3SetCanapeProjectParam = _libs["CANapAPI64.dll"].get("Asap3SetCanapeProjectParam", "stdcall")
    Asap3SetCanapeProjectParam.argtypes = [TAsap3Hdl, String, String, String]
    Asap3SetCanapeProjectParam.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 980
if _libs["CANapAPI64.dll"].has("Asap3FlashSetODXContainer", "stdcall"):
    Asap3FlashSetODXContainer = _libs["CANapAPI64.dll"].get("Asap3FlashSetODXContainer", "stdcall")
    Asap3FlashSetODXContainer.argtypes = [TAsap3Hdl, TModulHdl, String]
    Asap3FlashSetODXContainer.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 981
if _libs["CANapAPI64.dll"].has("Asap3FlashGetSessionCount", "stdcall"):
    Asap3FlashGetSessionCount = _libs["CANapAPI64.dll"].get("Asap3FlashGetSessionCount", "stdcall")
    Asap3FlashGetSessionCount.argtypes = [TAsap3Hdl, TModulHdl, POINTER(c_ulong)]
    Asap3FlashGetSessionCount.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 982
if _libs["CANapAPI64.dll"].has("Asap3FlashGetSessionName", "stdcall"):
    Asap3FlashGetSessionName = _libs["CANapAPI64.dll"].get("Asap3FlashGetSessionName", "stdcall")
    Asap3FlashGetSessionName.argtypes = [TAsap3Hdl, TModulHdl, c_ulong, String, POINTER(c_long)]
    Asap3FlashGetSessionName.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 983
if _libs["CANapAPI64.dll"].has("Asap3FlashGetJobCount", "stdcall"):
    Asap3FlashGetJobCount = _libs["CANapAPI64.dll"].get("Asap3FlashGetJobCount", "stdcall")
    Asap3FlashGetJobCount.argtypes = [TAsap3Hdl, TModulHdl, POINTER(c_ulong)]
    Asap3FlashGetJobCount.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 984
if _libs["CANapAPI64.dll"].has("Asap3FlashGetJobName", "stdcall"):
    Asap3FlashGetJobName = _libs["CANapAPI64.dll"].get("Asap3FlashGetJobName", "stdcall")
    Asap3FlashGetJobName.argtypes = [TAsap3Hdl, TModulHdl, c_ulong, String, POINTER(c_long)]
    Asap3FlashGetJobName.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 985
if _libs["CANapAPI64.dll"].has("Asap3FlashStartFlashJob", "stdcall"):
    Asap3FlashStartFlashJob = _libs["CANapAPI64.dll"].get("Asap3FlashStartFlashJob", "stdcall")
    Asap3FlashStartFlashJob.argtypes = [TAsap3Hdl, TModulHdl, String, String, String]
    Asap3FlashStartFlashJob.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 986
if _libs["CANapAPI64.dll"].has("Asap3FlashGetJobState", "stdcall"):
    Asap3FlashGetJobState = _libs["CANapAPI64.dll"].get("Asap3FlashGetJobState", "stdcall")
    Asap3FlashGetJobState.argtypes = [TAsap3Hdl, TModulHdl, POINTER(c_double), POINTER(c_int), POINTER(c_long), String, POINTER(c_ulong)]
    Asap3FlashGetJobState.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 987
if _libs["CANapAPI64.dll"].has("Asap3FlashStopJob", "stdcall"):
    Asap3FlashStopJob = _libs["CANapAPI64.dll"].get("Asap3FlashStopJob", "stdcall")
    Asap3FlashStopJob.argtypes = [TAsap3Hdl, TModulHdl]
    Asap3FlashStopJob.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 988
if _libs["CANapAPI64.dll"].has("Asap3SetInteractiveMode", "stdcall"):
    Asap3SetInteractiveMode = _libs["CANapAPI64.dll"].get("Asap3SetInteractiveMode", "stdcall")
    Asap3SetInteractiveMode.argtypes = [TAsap3Hdl, c_bool]
    Asap3SetInteractiveMode.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 989
if _libs["CANapAPI64.dll"].has("Asap3GetInteractiveMode", "stdcall"):
    Asap3GetInteractiveMode = _libs["CANapAPI64.dll"].get("Asap3GetInteractiveMode", "stdcall")
    Asap3GetInteractiveMode.argtypes = [TAsap3Hdl, POINTER(c_bool)]
    Asap3GetInteractiveMode.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 990
if _libs["CANapAPI64.dll"].has("Asap3RegisterCallBack", "stdcall"):
    Asap3RegisterCallBack = _libs["CANapAPI64.dll"].get("Asap3RegisterCallBack", "stdcall")
    Asap3RegisterCallBack.argtypes = [TAsap3Hdl, enum_ASAP3_EVENT_CODE, POINTER(None), c_ulong]
    Asap3RegisterCallBack.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 991
if _libs["CANapAPI64.dll"].has("Asap3UnRegisterCallBack", "stdcall"):
    Asap3UnRegisterCallBack = _libs["CANapAPI64.dll"].get("Asap3UnRegisterCallBack", "stdcall")
    Asap3UnRegisterCallBack.argtypes = [TAsap3Hdl, enum_ASAP3_EVENT_CODE]
    Asap3UnRegisterCallBack.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 996
if _libs["CANapAPI64.dll"].has("Asap3ConnectToCANape", "stdcall"):
    Asap3ConnectToCANape = _libs["CANapAPI64.dll"].get("Asap3ConnectToCANape", "stdcall")
    Asap3ConnectToCANape.argtypes = [POINTER(TAsap3Hdl), String, String, String]
    Asap3ConnectToCANape.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 997
if _libs["CANapAPI64.dll"].has("Asap3DisconnectFromCANape", "stdcall"):
    Asap3DisconnectFromCANape = _libs["CANapAPI64.dll"].get("Asap3DisconnectFromCANape", "stdcall")
    Asap3DisconnectFromCANape.argtypes = [TAsap3Hdl]
    Asap3DisconnectFromCANape.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 998
if _libs["CANapAPI64.dll"].has("Asap3OpenDisplayForFile", "stdcall"):
    Asap3OpenDisplayForFile = _libs["CANapAPI64.dll"].get("Asap3OpenDisplayForFile", "stdcall")
    Asap3OpenDisplayForFile.argtypes = [TAsap3Hdl, String]
    Asap3OpenDisplayForFile.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 999
if _libs["CANapAPI64.dll"].has("Asap3ReleaseResultList", "stdcall"):
    Asap3ReleaseResultList = _libs["CANapAPI64.dll"].get("Asap3ReleaseResultList", "stdcall")
    Asap3ReleaseResultList.argtypes = [TAsap3Hdl, c_int, POINTER(POINTER(c_char))]
    Asap3ReleaseResultList.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 1000
if _libs["CANapAPI64.dll"].has("Asap3OpenDisplay", "stdcall"):
    Asap3OpenDisplay = _libs["CANapAPI64.dll"].get("Asap3OpenDisplay", "stdcall")
    Asap3OpenDisplay.argtypes = [TAsap3Hdl, String, c_int, c_int, c_int, POINTER(POINTER(c_char)), String, String, c_int, POINTER(POINTER(c_char)), POINTER(POINTER(c_char)), String, POINTER(c_int), POINTER(POINTER(POINTER(c_char))), POINTER(c_int), POINTER(POINTER(POINTER(c_char))), POINTER(c_int), POINTER(POINTER(POINTER(c_char))), POINTER(POINTER(POINTER(c_char)))]
    Asap3OpenDisplay.restype = c_bool

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 1018
for _lib in _libs.values():
    if not _lib.has("dummy", "cdecl"):
        continue
    dummy = _lib.get("dummy", "cdecl")
    dummy.argtypes = []
    dummy.restype = None
    break

# <command-line>: 1
try:
    _REENTRANT = 1
except:
    pass

__const = c_int# <command-line>: 4

# <command-line>: 7
try:
    CTYPESGEN = 1
except:
    pass

bool = c_bool# C:/mingw/mingw32/lib/gcc/i686-w64-mingw32/8.1.0/include/stdbool.h: 33

# C:/mingw/mingw32/lib/gcc/i686-w64-mingw32/8.1.0/include/stdbool.h: 34
try:
    true = 1
except:
    pass

# C:/mingw/mingw32/lib/gcc/i686-w64-mingw32/8.1.0/include/stdbool.h: 35
try:
    false = 0
except:
    pass

# C:/mingw/mingw32/lib/gcc/i686-w64-mingw32/8.1.0/include/stdbool.h: 52
try:
    __bool_true_false_are_defined = 1
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 6
try:
    _MAX_PATH = 260
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 7
try:
    MAX_PATH = 260
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 9
try:
    AEC_CMD_NOT_SUP = 1
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 10
try:
    AEC_INTERFACE_NOTSUPPORTED = 2
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 11
try:
    AEC_CREATE_MEM_MAPPED_FILE = 3
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 12
try:
    AEC_WRITE_CMD = 4
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 13
try:
    AEC_READ_RESPONSE = 5
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 14
try:
    AEC_ASAP2_FILE_NOT_FOUND = 6
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 15
try:
    AEC_INVALID_MODULE_HDL = 7
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 16
try:
    AEC_ERR_OPEN_FILE = 8
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 17
try:
    AEC_UNKNOWN_OBJECT = 9
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 18
try:
    AEC_NO_DATABASE = 10
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 19
try:
    AEC_PAR_SIZE_OVERFLOW = 11
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 20
try:
    AEC_NOT_WRITE_ACCESS = 12
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 21
try:
    AEC_OBJECT_TYPE_DOESNT_MATCH = 13
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 22
try:
    AEC_NO_TASKS_OVERFLOW = 14
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 23
try:
    AEC_CCP_RESPONSE_SIZE_INVALID = 15
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 24
try:
    AEC_TIMEOUT_RESPONSE = 16
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 25
try:
    AEC_NO_VALUES_SAMPLED = 17
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 26
try:
    AEC_ACQ_CHNL_OVERRUN = 18
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 27
try:
    AEC_NO_RASTER_OVERFLOW = 19
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 28
try:
    AEC_CANAPE_CREATE_PROC_FAILED = 20
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 29
try:
    AEC_EXIT_DENIED_WHILE_ACQU = 21
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 30
try:
    AEC_WRITE_DATA_FAILED = 22
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 31
try:
    AEC_NO_RESPONSE_FROM_ECU = 23
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 32
try:
    AEC_ACQUIS_ALREADY_RUNNING = 24
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 33
try:
    AEC_ACQUIS_NOT_STARTED = 25
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 34
try:
    AEC_NO_AXIS_PTS_NOT_VALID = 27
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 35
try:
    AEC_SCRIPT_CMD_TO_LARGE = 28
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 36
try:
    AEC_SCRIPT_CMD_INVALID = 29
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 37
try:
    AEC_UNKNOWN_MODULE_NAME = 30
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 38
try:
    AEC_FIFO_INTERNAL_ERROR = 31
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 39
try:
    AEC_VERSION_ERROR = 32
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 40
try:
    AEC_ILLEGAL_DRIVER = 33
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 41
try:
    AEC_CALOBJ_READ_FAILED = 34
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 42
try:
    AEC_ACQ_STP_INIT_FAILED = 35
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 43
try:
    AEC_ACQ_STP_PROC_FAILED = 36
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 44
try:
    AEC_ACQ_STP_OVERFLOW = 37
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 45
try:
    AEC_ACQ_STP_TIME_OVER = 38
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 46
try:
    AEC_NOSERVER_ERRCODE = 40
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 47
try:
    AEC_ERR_OPEN_DATADESCFILE = 41
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 48
try:
    AEC_ERR_OPEN_DATAVERSFILE = 42
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 49
try:
    AEC_TO_MUCH_DISPLAYS_OPEN = 43
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 50
try:
    AEC_INTERNAL_CANAPE_ERROR = 44
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 51
try:
    AEC_CANT_OPEN_DISPLAY = 45
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 52
try:
    AEC_ERR_NO_PATTERNFILE_DEFINED = 46
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 53
try:
    AEC_ERR_OPEN_PATTERNFILE = 47
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 54
try:
    AEC_ERR_CANT_RELEASE_MUTEX = 48
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 55
try:
    AEC_WRONG_CANAPE_VERSION = 49
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 56
try:
    AEC_TCP_SERV_CONNECT_FAILED = 50
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 57
try:
    AEC_TCP_MISSING_CFG = 51
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 58
try:
    AEC_TCP_SERV_NOT_CONNECTED = 52
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 59
try:
    AEC_TCP_EXIT_NOTCLOSED = 53
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 60
try:
    AEC_FIFO_ALREADY_INIT = 54
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 61
try:
    AEC_ILLEGAL_OPERATION = 55
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 62
try:
    AEC_WRONG_TYPE = 56
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 63
try:
    AEC_NO_CANAPE_LICENSE = 57
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 64
try:
    AEC_REG_OPEN_KEY_FAILED = 58
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 65
try:
    AEC_REG_QUERY_VALUE_FAILED = 59
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 66
try:
    AEC_WORKDIR_ACCESS_FAILED = 60
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 67
try:
    AEC_INIT_COM_FAILED = 61
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 68
try:
    AEC_INIT_CMD_FAILED = 62
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 69
try:
    AEC_CANAPE_INVALID_PRG_PATH = 63
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 70
try:
    AEC_INVALID_ASAP3_HDL = 64
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 71
try:
    AEC_LOADING_FILE = 65
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 72
try:
    AEC_SAVING_FILE = 66
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 73
try:
    AEC_UPLOAD = 67
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 74
try:
    AEC_WRITE_VALUE_ERROR = 68
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 75
try:
    AEC_TMTF_NOT_FINSHED = 69
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 76
try:
    AEC_TMTF_SEQUENCE_ERROR = 70
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 77
try:
    AEC_TDBO_TYPE_ERROR = 71
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 78
try:
    AEC_EXECUTE_SERVICE_ERROR = 72
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 79
try:
    AEC_INVALID_DRIVERTYPE = 73
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 80
try:
    AEC_DIAG_INVALID_DRIVERTYPE = 74
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 81
try:
    AEC_DIAG_INVALID_BUSMESSAGE = 75
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 82
try:
    AEC_DIAG_INVALID_VARIANT = 76
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 83
try:
    AEC_DIAG_INVALID_DIAGSERVICE = 77
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 84
try:
    AEC_DIAG_ERR_EXECUTE_SERVICE = 78
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 85
try:
    AEC_DIAG_INVALID_PARAMS = 79
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 86
try:
    AEC_DIAG_UNKNOWN_PARAM_NAME = 80
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 87
try:
    AEC_DIAG_EXCEPTION_ERROR = 81
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 88
try:
    AEC_DIAG_INVALID_RESPONSE = 82
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 89
try:
    AEC_DIAG_UNKNOWN_PARAM_TYPE = 83
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 90
try:
    AEC_DIAG_NO_INFO_AVAILABLE = 84
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 91
try:
    AEC_DIAG_UNKNOWN_RESPHANDLE = 85
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 92
try:
    ACE_DIAG_WRONG_SERVICE_STATE = 86
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 93
try:
    AEC_DIAG_INVALID_INDEX_SIZE = 87
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 94
try:
    AEC_DIAG_INVALID_RESPONSETYPE = 88
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 95
try:
    AEC_FLASH_INVALID_MANAGER = 89
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 96
try:
    AEC_FLASH_OBJ_OUT_OF_RANGE = 90
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 97
try:
    AEC_FLASH_MANAGER_ERROR = 91
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 98
try:
    AEC_FLASH_ALLREADY_RUNNING = 92
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 99
try:
    AEC_FLASH_INVALID_APPNAME = 93
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 100
try:
    AEC_FUNCTION_NOT_SUPPORTED = 94
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 101
try:
    AEC_LICENSE_NOT_FOUND = 95
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 102
try:
    AEC_RECORDER_ALLREADY_EXISTS = 96
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 103
try:
    AEC_RECORDER_NOT_FOUND = 97
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 104
try:
    AEC_RECORDER_INDEX_OUTOFRANGE = 98
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 105
try:
    AEC_REMOVE_RECORDER_ERR = 99
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 106
try:
    AEC_INVALID_PARAMETER = 100
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 107
try:
    AEC_ERROR_CREATERECORDER = 101
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 108
try:
    AEC_ERROR_SETRECFILENAME = 102
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 109
try:
    AEC_ERROR_INVALID_TASKID = 103
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 110
try:
    AEC_DIAG_PARAM_SETERROR = 104
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 111
try:
    AEC_CNFG_WRONG_MODE = 105
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 112
try:
    AEC_CNFG_FILE_NOT_FOUND = 106
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 113
try:
    AEC_CNFG_FILE_INVALID = 107
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 114
try:
    AEC_INVALID_SCR_HANDLE = 108
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 115
try:
    AEC_REMOVE_SCR_HANDLE = 109
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 116
try:
    AEC_ERROR_DECALRE_SCR = 110
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 117
try:
    AEC_ERROR_RESUME_SUPPORTED = 111
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 118
try:
    AEC_UNDEFINED_CHANNEL = 112
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 119
try:
    AEC_ERR_DRIVER_CONFIG = 113
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 120
try:
    AEC_ERR_DCB_EXPORT = 114
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 121
try:
    ACE_NOT_AVAILABLE_WHILE_ACQ = 115
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 122
try:
    ACE_NOT_MISSING_LICENSE = 116
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 123
try:
    ACE_EVENT_ALLREADY_REGISERED = 117
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 124
try:
    AEC_OBJECT_ALLREADY_DEFINED = 118
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 125
try:
    AEC_CAL_NOT_ALLOWED = 119
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 126
try:
    AEC_DIAG_UNDEFINED_JOB = 120
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 127
try:
    AEC_ERROR_MODAL_DIALOG = 121
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 128
try:
    AEC_ERROR_CHANNEL_ASSIGNMENT = 122
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 129
try:
    AEC_ERROR_STRUCTURE_OBJECT = 123
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 130
try:
    AEC_NETWORK_NOT_FOUND = 124
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 131
try:
    AEC_ERROR_LOADING_LABELLIST = 125
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 132
try:
    AEC_ERROR_CONV_FILE_ACCESS = 126
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 133
try:
    AEC_ERROR_COMPLEX_RESPONSES = 127
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 134
try:
    AEC_ERROR_INIPATH = 128
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 135
try:
    AEC_USUPPORTED_INTERFACE_ID = 129
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 136
try:
    AEC_INSUFFICENT_BUFFERSIZE = 130
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 137
try:
    AEC_PATCHENTRY_NOT_FOUND = 131
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 138
try:
    AEC_PATCHSECTION_NOT_FOUND = 132
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 139
try:
    AEC_SEC_MANAGER_ERROR = 133
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 140
try:
    ACE_CHANNEL_OPTIMIZED = 134
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 141
try:
    ACE_ERR_PROFILE_ID = 135
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 142
try:
    ACE_ERR_UNSUPPORTED_TYPE = 136
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 143
try:
    AEC_LAST_ERRCODE = 137
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 527
try:
    TDBE_VALUE_SCALAR = 1
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 528
try:
    TDBE_VALUE_CURVE = 2
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 529
try:
    TDBE_VALUE_MAP = 4
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 530
try:
    TDBE_VALUE_AXIS = 8
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 531
try:
    TDBE_VALUE_ASCII = 16
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 532
try:
    TDBE_VALUE_VALBLK = 32
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 533
try:
    TDBE_VALUE_ALL = (((((TDBE_VALUE_SCALAR | TDBE_VALUE_CURVE) | TDBE_VALUE_MAP) | TDBE_VALUE_AXIS) | TDBE_VALUE_ASCII) | TDBE_VALUE_VALBLK)
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 534
try:
    ASAP3_INVALID_HDL = (TAsap3Hdl (ord_if_char(0))).value
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 535
try:
    ASAP3_UNUSED_SECURITY = (c_uint (ord_if_char(0))).value
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 536
try:
    ASAP3_NO_SECURITY_JOB = ''
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 548
try:
    ASAP3_INVALID_MODULE_HDL = (-1)
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 607
try:
    DLL_INTERFACE_VERSION = '02.03.01.Windows95/WindowsNT.1  '
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 608
try:
    CANAPE_API_MAIN_VESION = 2
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 609
try:
    CANAPE_API_SUB_VESION = 3
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 610
try:
    CANAPE_API_RELEASE = 1
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 611
try:
    CANAPE_API_OS_VERSION = 'Windows95/WindowsNT'
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 612
try:
    CANAPE_API_OS_RELEASE = 1
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 614
try:
    CUSTOMER_ID = 'Unknown'
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 617
try:
    MAX_OS_VERSION = 50
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 632
try:
    DEV_CAN1 = 1
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 633
try:
    DEV_CAN2 = 2
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 634
try:
    DEV_CAN3 = 3
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 635
try:
    DEV_CAN4 = 4
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 636
try:
    DEV_CAN5 = 5
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 637
try:
    DEV_CAN6 = 6
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 638
try:
    DEV_CAN7 = 7
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 639
try:
    DEV_CAN8 = 8
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 640
try:
    DEV_CAN20 = 20
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 641
try:
    DEV_FLX1 = 31
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 642
try:
    DEV_FLX2 = 32
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 643
try:
    DEV_FLX3 = 33
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 644
try:
    DEV_FLX4 = 34
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 645
try:
    DEV_FLX5 = 35
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 646
try:
    DEV_FLX6 = 36
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 647
try:
    DEV_FLX7 = 37
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 648
try:
    DEV_FLX8 = 38
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 649
try:
    DEV_LIN1 = 61
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 650
try:
    DEV_LIN2 = 62
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 651
try:
    DEV_LIN3 = 63
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 652
try:
    DEV_LIN4 = 64
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 653
try:
    DEV_LIN5 = 65
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 654
try:
    DEV_LIN6 = 66
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 655
try:
    DEV_LIN7 = 67
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 656
try:
    DEV_LIN8 = 68
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 657
try:
    DEV_VX_CAN1 = 81
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 658
try:
    DEV_VX_CAN2 = 82
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 659
try:
    DEV_VX_CAN3 = 83
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 660
try:
    DEV_VX_CAN4 = 84
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 661
try:
    DEV_VX_TCP = 85
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 662
try:
    DEV_VX_UDP = 86
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 663
try:
    DEV_SXI1 = 91
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 664
try:
    DEV_SXI2 = 92
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 665
try:
    DEV_SXI3 = 93
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 666
try:
    DEV_SXI4 = 94
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 667
try:
    DEV_SXI5 = 95
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 668
try:
    DEV_SXI6 = 96
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 669
try:
    DEV_SXI7 = 97
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 670
try:
    DEV_SXI8 = 98
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 671
try:
    DEV_USB = 110
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 672
try:
    DEV_CANFD1 = 121
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 673
try:
    DEV_CANFD2 = 122
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 674
try:
    DEV_CANFD3 = 123
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 675
try:
    DEV_CANFD4 = 124
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 676
try:
    DEV_CANFD5 = 125
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 677
try:
    DEV_CANFD6 = 126
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 678
try:
    DEV_CANFD7 = 127
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 679
try:
    DEV_CANFD8 = 128
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 680
try:
    DEV_CANFD9 = 129
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 681
try:
    DEV_TCP = 255
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 682
try:
    DEV_UDP = 256
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 683
try:
    DEV_USERDEFINED = 261
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 684
try:
    DEV_VX_ETHERNET1 = 271
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 685
try:
    DEV_VX_ETHERNET2 = 272
except:
    pass

# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 686
try:
    DEV_DAIO_DLL = 280
except:
    pass

TApplicationID = struct_TApplicationID# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 186

DiagJobResponse = struct_DiagJobResponse# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 237

PValues = union_PValues# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 246

DiagNumericParameter = struct_DiagNumericParameter# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 242

DiagNotificationStruct = struct_DiagNotificationStruct# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 255

TMeasurementListEntry = struct_TMeasurementListEntry# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 261

MeasurementListEntries = struct_MeasurementListEntries# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 273

DBObjectInfo = struct_DBObjectInfo# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 288

DBFileInfo = struct_DBFileInfo# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 289

TLayoutCoeffs = struct_TLayoutCoeffs# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 295

SecProfileEntry = struct_SecProfileEntry# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 307

TConverterInfo = struct_TConverterInfo# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 484

tAsap3Hdl = struct_tAsap3Hdl# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 537

tSampleObject = struct_tSampleObject# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 574

tSampleBlockObject = struct_tSampleBlockObject# C:\\Users\\sim\\Desktop\\canapePY_COM\\ctypes_canapedll_002\\CANapAPI_stripped.h: 567

# No inserted files

# No prefix-stripping

