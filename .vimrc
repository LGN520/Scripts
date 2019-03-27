"去掉vi的一致性"
set nocompatible
" 显示行号"
set number
" 隐藏滚动条"    
set guioptions-=r 
set guioptions-=L
set guioptions-=b
"隐藏顶部标签栏"
set showtabline=0
"设置字体"
set guifont=Monaco:h13         
syntax on   "开启语法高亮"
" let g:solarized_termcolors=256  "solarized主题设置在终端下的设置"
set background=dark     "设置背景色"
" colorscheme solarized
set nowrap  "设置不折行"
set fileformat=unix "设置以unix的格式保存文件"
set cindent     "设置C样式的缩进格式"
set tabstop=4   "设置table长度"
set shiftwidth=4        "同上"
set showmatch   "显示匹配的括号"
set scrolloff=5     "距离顶部和底部5行"
set laststatus=2    "命令行为两行"
set fenc=utf-8      "文件编码"
set backspace=2
set mouse=a     "启用鼠标"
set selection=exclusive
set selectmode=mouse,key
set matchtime=5
set ignorecase      "忽略大小写"
set incsearch
set hlsearch        "高亮搜索项"
set noexpandtab     "不允许扩展table"
set whichwrap+=<,>,h,l
set autoread
set cursorline      "突出显示当前行"
set cursorcolumn        "突出显示当前列"

" Configuration of Vundle"
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" Vundle: vim plugin manager
Plugin 'VundleVim/Vundle.vim'
" Solarized colorscheme
" Plugin 'altercation/vim-colors-solarized'
" YCM
Plugin 'Valloric/YouCompleteMe'
" powerline
Plugin 'Lokaltog/vim-powerline'
" NERD Tree
Plugin 'scrooloose/nerdtree'
" Base utility
Plugin 'L9'
" IndentLine
Plugin 'Yggdroot/indentLine'
" AutoPep8
Plugin 'tell-k/vim-autopep8'
" AutoPairs
Plugin 'jiangmiao/auto-pairs'
" nerd commenter
Plugin 'scrooloose/nerdcommenter'
" ctrlp.vim
Plugin 'ctrlpvim/ctrlp.vim'
" ctrlsf.vim
Plugin 'dyng/ctrlsf.vim'
" tagbar
Plugin 'majutsushi/tagbar'
call vundle#end()
filetype plugin indent on

" Configuration of YouCompleteMe"
"默认配置文件路径"
let g:ycm_global_ycm_extra_conf = '~/.vim/bundle/YouCompleteMe/.ycm_extra_conf.py'
""打开vim时不再询问是否加载ycm_extra_conf.py配置"
let g:ycm_confirm_extra_conf=0
set completeopt=longest,menu
"python解释器路径"
let g:ycm_path_to_python_interpreter='/usr/bin/python'
""是否开启语义补全"
let g:ycm_seed_identifiers_with_syntax=1
"是否在注释中也开启补全"
let g:ycm_complete_in_comments=1
let g:ycm_collect_identifiers_from_comments_and_strings = 0
""开始补全的字符数"
let g:ycm_min_num_of_chars_for_completion=2
"补全后自动关机预览窗口"
let g:ycm_autoclose_preview_window_after_completion=1
"" 禁止缓存匹配项,每次都重新生成匹配项"
let g:ycm_cache_omnifunc=0
"字符串中也开启补全"
let g:ycm_complete_in_strings = 1
""离开插入模式后自动关闭预览窗口"
autocmd InsertLeave * if pumvisible() == 0|pclose|endif

" Configuration of NERDTree
"F2开启和关闭树"
map <F2> :NERDTreeToggle<CR>
let NERDTreeChDirMode=1
""显示书签"
let NERDTreeShowBookmarks=1
"设置忽略文件类型"
let NERDTreeIgnore=['\~$', '\.pyc$', '\.swp$']
""窗口大小"
let NERDTreeWinSize=25

" Configuration IndentLine
"缩进指示线"
let g:indentLine_char='┆'
let g:indentLine_enabled = 1

" Configuration autopep
""autopep8设置"
let g:autopep8_disable_show_diff=1

" Configuration of nerdcommenter
let mapleader='/'
map <F4> <leader>ci <CR>

" Configuration of tagbar
map <F3> :TagbarToggle<CR>

" Configuration of ctrlsf
let g:ctrlsf_default_root="~/projects"

"--ctags setting--
" 按下F5重新生成tag文件，并更新taglist
map <F5> :!ctags -R --c++-kinds=+p --fields=+iaS --extra=+q .<CR><CR> :TlistUpdate<CR>
imap <F5> <ESC>:!ctags -R --c++-kinds=+p --fields=+iaS --extra=+q.<CR><CR> :TlistUpdate<CR>
set tags=tags
set tags+=./tags "add current directory's generated tags file
set tags+=/usr/lib/tags "add new tags file(刚刚生成tags的路径，在ctags -R 生成tags文件后，不要将tags移动到别的目录，否则ctrl+］时，会提示找不到源码文件)"
