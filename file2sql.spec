# -*- mode: python -*-

block_cipher = None


a = Analysis(['file2sql.py'],
             pathex=['D:\\Documents\\projects\\psc-file2sql'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='file2sql',
          debug=False,
          strip=False,
          upx=True,
          console=True )
