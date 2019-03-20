# vim_python_IDE
### 升级vim
centos7.3自带的vim是7.4.*版本, YouCompleteMe需要Vim 7.4.1578+
我这里编译安装vim8.0


```

# 移除旧版本
sudo yum remove vim -y
# 安装必要组件
sudo yum install ncurses-devel python-devel -y
# 下载源码编译安装
git clone https://github.com/vim/vim.git
cd vim/src
# 根据自己实际情况设置编译参数
./configure --with-features=huge --enable-pythoninterp=yes --enable-cscope --enable-fontset --with-python-config-dir=/usr/lib64/python2.7/config --enable-python3interp=yes --with-python-config-dir=/usr/lib/python3.6/config --enable-multibyte --prefix=/usr/local/vim/

make -j2 && make install
```

编译参数说明： 
- [ ] –with-features=huge：支持最大特性 
- [ ] –enable-rubyinterp：打开对ruby编写的插件的支持 
- [ ] –enable-pythoninterp：打开对python编写的插件的支持 
- [ ] –enable-python3interp：打开对python3编写的插件的支持 
- [ ] –enable-luainterp：打开对lua编写的插件的支持 
- [ ] –enable-perlinterp：打开对perl编写的插件的支持 
- [ ] –enable-multibyte：打开多字节支持，可以在Vim中输入中文 
- [ ] –enable-cscope：打开对cscope的支持 
- [ ] –with-python-config-dir=/usr/lib64/python2.7/config 指定python 路径 
- [ ] –with-python-config-dir=/usr/lib64/python3.5/config 指定python3路径

注意：必须带上Python编写插件支持，最好带上Python路径，否则使用时会报这个错误：YouCompleteMe unavailable: requires Vim compiled with Python (2.6+ or 3.6+) support

安装完成后，vim就安装在了/usr/local/vim/bin，添加环境变量，把该目录加入到PATH方便terminal全局使用


```
[root@aiker ~]# cat /etc/profile.d/vim.sh 
export PATH=$PATH:/usr/local/vim/bin/
```
查看版本和支持信息：

```
[root@aiker ~]# vim --version
VIM - Vi IMproved 8.1 (2018 May 18, compiled Aug 20 2018 03:23:45)
Included patches: 1-299
Compiled by root@aiker
Huge version without GUI.  Features included (+) or not (-):
+acl               +extra_search      +mouse_netterm     +tag_old_static
+arabic            +farsi             +mouse_sgr         -tag_any_white
+autocmd           +file_in_path      -mouse_sysmouse    -tcl
+autochdir         +find_in_path      +mouse_urxvt       +termguicolors
-autoservername    +float             +mouse_xterm       +terminal
-balloon_eval      +folding           +multi_byte        +terminfo
+balloon_eval_term -footer            +multi_lang        +termresponse
-browse            +fork()            -mzscheme          +textobjects
++builtin_terms    +gettext           +netbeans_intg     +timers
+byte_offset       -hangul_input      +num64             +title
+channel           +iconv             +packages          -toolbar
+cindent           +insert_expand     +path_extra        +user_commands
-clientserver      +job               -perl              +vartabs
-clipboard         +jumplist          +persistent_undo   +vertsplit
+cmdline_compl     +keymap            +postscript        +virtualedit
+cmdline_hist      +lambda            +printer           +visual
+cmdline_info      +langmap           +profile           +visualextra
+comments          +libcall           +python            +viminfo
+conceal           +linebreak         -python3           +vreplace
+cryptv            +lispindent        +quickfix          +wildignore
+cscope            +listcmds          +reltime           +wildmenu
+cursorbind        +localmap          +rightleft         +windows
+cursorshape       -lua               -ruby              +writebackup
+dialog_con        +menu              +scrollbind        -X11
+diff              +mksession         +signs             -xfontset
+digraphs          +modify_fname      +smartindent       -xim
-dnd               +mouse             +startuptime       -xpm
-ebcdic            -mouseshape        +statusline        -xsmp
+emacs_tags        +mouse_dec         -sun_workshop      -xterm_clipboard
+eval              -mouse_gpm         +syntax            -xterm_save
+ex_extra          -mouse_jsbterm     +tag_binary        
   system vimrc file: "$VIM/vimrc"
     user vimrc file: "$HOME/.vimrc"
 2nd user vimrc file: "~/.vim/vimrc"
      user exrc file: "$HOME/.exrc"
       defaults file: "$VIMRUNTIME/defaults.vim"
  fall-back for $VIM: "/usr/local/vim/share/vim"
Compilation: gcc -std=gnu99 -c -I. -Iproto -DHAVE_CONFIG_H     -g -O2 -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1       
Linking: gcc -std=gnu99   -L/usr/local/lib -Wl,--as-needed -o vim        -lm -ltinfo -lnsl  -lselinux  -ldl    -L/usr/lib64/python2.7/config -lpython2.7 -lpthread -ldl -lutil -lm -Xlinker -export-dynamic  
```

### 安装Vundle和YouCompleteMe

Vundle是Vim的插件管理工具，官方文档：https://github.com/VundleVim/Vundle.vim

安装步骤很简单：


```
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

#### 添加颜色主题方案
我这里使用monokai 配色方案 ：https://github.com/sickill/vim-monokai

下载对应的monokai.vim 文件 放到 ~/.vim/colors/ 即可


```
mkdir ~/.vim/colors
wget -O ~/.vim/colors/monokai.vim https://raw.githubusercontent.com/sickill/vim-monokai/master/colors/monokai.vim
```

```
git clone https://github.com/donxan/vim_python_IDE.git
```


### 安装插件

打开任意一vim编辑窗口，使用命令模式键入以下命令即可实现对应功能


```
:PluginList - 列出所有已配置的插件
:PluginInstall - 安装插件,追加 `!` 用以更新或使用
:PluginUpdate:PluginSearch foo - 搜索 foo ; 追加 `!` 清除本地缓存
:PluginClean - 清除未使用插件,需要确认; 追加 `!` 自动批准移除未使用插件
:h vundle 获取更多细节和wiki以及FAQ
```
或者通过以下快速安装：

```
 vim +PluginInstall +qall
```
### 附加
增加clang:添加C语言家族语法补全功能

```
sudo yum install cmake -y
cd ~/.vim/plugin/YouCompleteMe  
./install.py --clang-completer
```
