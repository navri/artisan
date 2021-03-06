# -*- mode: python -*-

block_cipher = None

ARTISAN_SRC = r'C:\Users\luther\Desktop\src'
PYTHON35 = r'C:\Program Files\Python35'
NAME = 'artisan'

##
TARGET = 'dist\\' + NAME + '\\'
PYTHON_PACKAGES = PYTHON35 + r'\Lib\site-packages'
PYQT_QT = PYTHON_PACKAGES + r'\PyQt5\Qt'
PYQT_QT_BIN = PYQT_QT + r'\bin'
PYQT_QT_TRANSLATIONS = PYQT_QT + r'\translations'
YOCTO_BIN = PYTHON_PACKAGES + r'\yoctopuce\cdll'

#os.system(PYTHON35 + r'\Scripts\pylupdate5 artisan.pro')

a = Analysis(['artisan.py'],
             pathex=[PYQT_QT_BIN, ARTISAN_SRC],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,cipher=block_cipher)


exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name=NAME,
          debug=False,
          strip=False, # =True fails
          upx=True, # not installed
          icon='artisan.ico',
          console=False ) # was True

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False, # =True fails
               upx=True, # not installed
               name=NAME)


# assumes the Microsoft Visual C++ 2015 Redistributable Package (x64), vc_redist.x64.exe, is located above the source directory
os.system(r'copy ..\vc_redist.x64.exe ' + TARGET)

os.system('copy README.txt ' + TARGET)
os.system('copy LICENSE.txt ' + TARGET)
#os.system('copy qt-win.conf ' + TARGET + 'qt.conf')
os.system('mkdir ' + TARGET + 'Wheels')
os.system('mkdir ' + TARGET + r'Wheels\Cupping')
os.system('mkdir ' + TARGET + r'Wheels\Other')
os.system('mkdir ' + TARGET + r'Wheels\Roasting')
os.system(r'copy Wheels\Cupping\* ' + TARGET + r'Wheels\Cupping')
os.system(r'copy Wheels\Other\* ' + TARGET + r'Wheels\Other')
os.system(r'copy Wheels\Roasting\* ' + TARGET + r'Wheels\Roasting')

os.system('mkdir ' + TARGET + 'translations')
os.system(r'copy translations\*.qm ' + TARGET + 'translations')
for tr in [
    'qt_ar.qm',
    'qt_de.qm',
    'qt_es.qm',
    'qt_fi.qm',
    'qt_fr.qm',
    'qt_he.qm',
    'qt_hu.qm',
    'qt_it.qm',
    'qt_ja.qm',
    'qt_ko.qm',
    'qt_pt.qm',
    'qt_pl.qm',
    'qt_ru.qm',
    'qt_ru.qm',
    'qt_sv.qm',
    'qt_zh_CN.qm',
    'qt_zh_TW.qm',
    ]:
  os.system(r'copy "' + PYQT_QT_TRANSLATIONS + '\\' + tr + '" ' + TARGET + 'translations')

os.system('rmdir /q /s ' + TARGET + 'mpl-data\\sample_data')
# YOCTO HACK BEGIN: manually copy over the dlls
os.system(r'mkdir ' + TARGET + 'lib')
os.system(r'copy "' + YOCTO_BIN + r'\yapi.dll" ' + TARGET + 'lib')
os.system(r'copy "' + YOCTO_BIN + r'\yapi64.dll" ' + TARGET + 'lib')
# YOCTO HACK END

for fn in [
    'artisan.png',
    'artisanAlarms.ico',
    'artisanProfile.ico',
    'artisanPalettes.ico',
    'artisanSettings.ico',
    'artisanWheel.ico',
    r'includes\Humor-Sans.ttf',
    r'includes\alarmclock.eot',
    r'includes\alarmclock.svg',
    r'includes\alarmclock.ttf',
    r'includes\alarmclock.woff',
    r'includes\artisan.tpl',
    r'includes\bigtext.js',
    r'includes\sorttable.js',
    r'includes\report-template.htm',
    r'includes\roast-template.htm',
    r'includes\ranking-template.htm',
    r'includes\jquery-1.11.1.min.js',
    ]:
  os.system('copy ' + fn + ' ' + TARGET)

os.system(r'mkdir ' +  TARGET + 'Machines')
os.system(r'xcopy includes\Machines ' + TARGET + 'Machines /y /S')



