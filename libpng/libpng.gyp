{
  'variables': {
    'depth': '../..',
  },
  'includes': [
    #'../../build/common.gypi',
    #'../../build/external_code.gypi',
  ],
  'targets': [
    {
      'target_name': 'libpng',
      'type': 'static_library',
      'dependencies': [
        '../zlib/zlib.gyp:zlib',
      ],
      'defines': [
        'CHROME_PNG_WRITE_SUPPORT',
        'PNG_USER_CONFIG',
      ],
      'sources': [
        'png.c',
        'png.h',
        'pngconf.h',
        'pngerror.c',
        'pngget.c',
        'pngmem.c',
        'pngpread.c',
        'pngread.c',
        'pngrio.c',
        'pngrtran.c',
        'pngrutil.c',
        'pngset.c',
        'pngtrans.c',
        'pngwio.c',
        'pngwrite.c',
        'pngwtran.c',
        'pngwutil.c',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '.',
        ],
        'defines': [
          'CHROME_PNG_WRITE_SUPPORT',
          'PNG_USER_CONFIG',
        ],
      },
      'export_dependent_settings': [
        '../zlib/zlib.gyp:zlib',
      ],
    },
  ],
}
