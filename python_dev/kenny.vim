" local syntax file - set colors on a per-machine basis:
" vim: tw=0 ts=4 sw=4
" Vim color file

set background=dark

hi clear

if exists("syntax_on")
  syntax reset
endif

let g:colors_name = "kenny"

hi Normal                       ctermfg=White           guifg=cyan      guibg=black
hi Comment      term=bold       ctermfg=LightGrey       guifg=#80a0ff
hi Constant     term=underline  ctermfg=Magenta         guifg=Magenta
hi Special      term=bold       ctermfg=DarkMagenta     guifg=Red
hi Identifier   term=underline  cterm=bold              ctermfg=Cyan guifg=#40ffff
hi Statement                    ctermfg=LightRed
hi Decorator                    ctermfg=LightBlue
hi Keyword      term=bold       ctermfg=LightRed        gui=bold        guifg=#aa4444
hi PreProc      term=underline  ctermfg=LightRed        guifg=#ff80ff
hi Type         term=underline  ctermfg=LightGreen      guifg=#60ff60   gui=bold
hi Function     term=bold       ctermfg=White           guifg=White
hi Repeat       term=underline  ctermfg=White           guifg=white
hi Operator                     ctermfg=LightRed        guifg=Red
hi String                       ctermfg=Green           guifg=Red
hi Number                       ctermfg=LightBlue               guifg=Red
hi Boolean                      ctermfg=LightBlue               guifg=Red
hi Float                        ctermfg=LightBlue               guifg=Red
hi Ignore                       ctermfg=black           guifg=bg
hi Error        term=reverse ctermbg=Red ctermfg=White guibg=Red guifg=White
hi Todo         term=standout ctermbg=Yellow ctermfg=Black guifg=Blue guibg=Yellow
hi Character                    ctermfg=LightRed        guifg=Red
hi Conditional                  ctermfg=LightRed        guifg=Red
hi Label                        ctermfg=LightRed        guifg=Red
hi Include                      ctermfg=LightRed        guifg=Red
hi Repeat                       ctermfg=LightRed        guifg=Red
hi Special                      ctermfg=LightRed        guifg=Red
hi SpecialChar                  ctermfg=LightRed        guifg=Red
hi Define                       ctermfg=LightRed        guifg=Red
