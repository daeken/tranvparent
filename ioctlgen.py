def ioctls(**kwargs):
	with file('ioctls.cpp', 'w') as fp:
		print >>fp, '// Autogenerated by ioctlgen.py'
		print >>fp
		print >>fp, '#include "nvwrapper.h"'
		for name, elems in kwargs.items():
			print >>fp
			print >>fp, 'const char *ioctl2str(%s value) {' % name
			print >>fp, '\tswitch(value) {'
			for k, v in elems.items():
				print >>fp, '\tcase %s::%s:' % (name, k)
				print >>fp, '\t\treturn "%s";' % k
			print >>fp, '\tdefault:'
			print >>fp, '\t\treturn "UNKNOWN";'
			print >>fp, '\t}'
			print >>fp, '}'

	with file('ioctls.h', 'w') as fp:
		print >>fp, '// Autogenerated by ioctlgen.py'
		print >>fp
		print >>fp, '#pragma once'
		print >>fp
		print >>fp, '#include "nvwrapper.h"'
		for name, elems in kwargs.items():
			print >>fp
			print >>fp, 'enum %s {' % name
			for i, (k, v) in enumerate(elems.items()):
				print >>fp, '\t%s = 0x%08X%s' % (k, v, ', ' if i < len(elems) - 1 else '')
			print >>fp, '};'
			print >>fp, 'const char *ioctl2str(%s value);' % name

_IOC_NONE = 0
_IOC_WRITE = 1
_IOC_READ = 2

_IOC_NRSHIFT = 0
_IOC_TYPESHIFT = 8
_IOC_SIZESHIFT = 16
_IOC_DIRSHIFT = 30

_IOC = lambda dir, type, nr, size: (
		(dir << _IOC_DIRSHIFT) | 
		((type if isinstance(type, int) else ord(type)) << _IOC_TYPESHIFT) | 
		(nr << _IOC_NRSHIFT) | 
		(size << _IOC_SIZESHIFT)
	)

_IO = lambda type, nr: _IOC(_IOC_NONE, type, nr, 0)
_IOR = lambda type, nr, size: _IOC(_IOC_READ, type, nr, size)
_IOW = lambda type, nr, size: _IOC(_IOC_WRITE, type, nr, size)
_IOWR = lambda type, nr, size: _IOC(_IOC_READ | _IOC_WRITE, type, nr, size)


NVGPU_GPU_IOCTL_MAGIC = 'G'

ioctls(
	LinuxNvhostCtrlGpuIoctl=dict(
		NVGPU_GPU_IOCTL_ZCULL_GET_CTX_SIZE=_IOR(NVGPU_GPU_IOCTL_MAGIC, 1, 4), 
		NVGPU_GPU_IOCTL_ZCULL_GET_INFO=_IOR(NVGPU_GPU_IOCTL_MAGIC, 2, 40), 
		NVGPU_GPU_IOCTL_ZBC_SET_TABLE=_IOW(NVGPU_GPU_IOCTL_MAGIC, 3, 44), 
		NVGPU_GPU_IOCTL_ZBC_QUERY_TABLE=_IOWR(NVGPU_GPU_IOCTL_MAGIC, 4, 52), 
		NVGPU_GPU_IOCTL_GET_CHARACTERISTICS=_IOWR(NVGPU_GPU_IOCTL_MAGIC, 5, 188), 
		NVGPU_GPU_IOCTL_PREPARE_COMPRESSIBLE_READ=_IOWR(NVGPU_GPU_IOCTL_MAGIC, 6, 80), 
		NVGPU_GPU_IOCTL_MARK_COMPRESSIBLE_WRITE=_IOWR(NVGPU_GPU_IOCTL_MAGIC, 7, 32), 
		NVGPU_GPU_IOCTL_ALLOC_AS=_IOWR(NVGPU_GPU_IOCTL_MAGIC, 8, 8), 
		NVGPU_GPU_IOCTL_OPEN_TSG=_IOWR(NVGPU_GPU_IOCTL_MAGIC, 9, 8), 
		NVGPU_GPU_IOCTL_GET_TPC_MASKS=_IOWR(NVGPU_GPU_IOCTL_MAGIC, 10, 16), 
		NVGPU_GPU_IOCTL_OPEN_CHANNEL=_IOWR(NVGPU_GPU_IOCTL_MAGIC, 11, 4), 
		NVGPU_GPU_IOCTL_FLUSH_L2=_IOWR(NVGPU_GPU_IOCTL_MAGIC, 12, 8), 
		NVGPU_GPU_IOCTL_INVAL_ICACHE=_IOWR(NVGPU_GPU_IOCTL_MAGIC, 13, 8), 
		NVGPU_GPU_IOCTL_SET_MMUDEBUG_MODE=_IOWR(NVGPU_GPU_IOCTL_MAGIC, 14, 8), 
		NVGPU_GPU_IOCTL_SET_SM_DEBUG_MODE=_IOWR(NVGPU_GPU_IOCTL_MAGIC, 15, 16), 
		NVGPU_GPU_IOCTL_WAIT_FOR_PAUSE=_IOWR(NVGPU_GPU_IOCTL_MAGIC, 16, 8), 
		NVGPU_GPU_IOCTL_GET_TPC_EXCEPTION_EN_STATUS=_IOWR(NVGPU_GPU_IOCTL_MAGIC, 17, 8), 
		NVGPU_GPU_IOCTL_NUM_VSMS=_IOWR(NVGPU_GPU_IOCTL_MAGIC, 18, 8), 
		NVGPU_GPU_IOCTL_VSMS_MAPPING=_IOWR(NVGPU_GPU_IOCTL_MAGIC, 19, 8)
	)
)
