# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['iwbtd.py','math_funcs.py','scenes.py','resources.py'],
    pathex=[],
    binaries=[],
    datas=[(r'E:\\projects for jetbrain\\pypro\\venv\\Scripts\\iwanna hard\\images','images'),
	(r'E:\\projects for jetbrain\\pypro\\venv\\Scripts\\iwanna hard\\sounds','sounds'),
                (r'E:\\projects for jetbrain\\pypro\\venv\\Scripts\\iwanna hard\\music','music'),
                (r'E:\\projects for jetbrain\\pypro\\venv\\Scripts\\iwanna hard\\fonts','fonts')
	],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='iwbtd',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon="E:\\projects for jetbrain\\pypro\\venv\\Scripts\\iwanna hard\\pic.ico",
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='iwbtd',
)
