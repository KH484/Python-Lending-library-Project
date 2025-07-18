parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
#git clrs
export PS1="\u@\h \[\033[00;97m\]\w \[\e[00;36m\]\$(parse_git_branch)\[\e[96m\]$ "


