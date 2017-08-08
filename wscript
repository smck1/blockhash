APPNAME = 'blockhash'
VERSION = '0.1'

top = '.'
out = 'build'

def options(opt):
    opt.load('compiler_cxx boost')

def configure(conf):
    conf.load('compiler_cxx boost')
    conf.env.LIB_BOOST = ['boost_system', 'boost_thread', 'boost_filesystem']
    conf.check_cc(lib='m')
    conf.check_cfg(package='MagickWand', args=['--cflags', '--libs'])




    if conf.check_cfg(modversion='MagickWand') >= '7':
        conf.define('MAGICKWAND_V7', True)

def build(bld):
    bld(
        features='cxx cxxprogram',
        source='blockhash.cpp',
        target='blockhash',
        use=['MAGICKWAND', 'M', 'BOOST'],
        cflags=['-O3'],
        cxxflags=['-std=c++11','-fpermissive']
    )
