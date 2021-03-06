{
  'targets': [
    {
      'target_name': 'zlib',
      'type': 'static_library',
      'sources': [
        'crc32.h',
        'deflate.h',
        'gzguts.h',
        'inffast.h',
        'inffixed.h',
        'inflate.h',
        'inftrees.h',
        'trees.h',
        'zconf.h',
        'zlib.h',
        'zutil.h',

        'adler32.c',
        'compress.c',
        'crc32.c',
        'deflate.c',
        'gzclose.c',
        'gzlib.c',
        'gzread.c',
        'gzwrite.c',
        'infback.c',
        'inffast.c',
        'inflate.c',
        'inftrees.c',
        'trees.c',
        'uncompr.c',
        'zutil.c',
      ],
      'vs_props': [ '../../build/external_code.vsprops' ],
      'dependent_settings': {
        'include_dirs': [
          '.',
        ],
      },
    },
  ],
}
