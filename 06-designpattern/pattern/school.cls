\ProvidesClass{school}
\LoadClass[a4paper,10pt]{article}
% = Packages
% == Format
\RequirePackage{a4wide}
\RequirePackage{booktabs}
\RequirePackage[marginal, norule, perpage]{footmisc}
\RequirePackage{titling}
\RequirePackage{lastpage}
% === Language
\RequirePackage[ngerman]{babel}
% === Font
\RequirePackage[utf8]{inputenc}
\RequirePackage{microtype}
\RequirePackage[T1]{fontenc}
\RequirePackage{mathptmx}
% === Color
\RequirePackage[dvipsnames]{xcolor}
% === Header
\RequirePackage{fancyhdr}
% == Math
\RequirePackage{amssymb}
\RequirePackage{mathtools}
% == Graphics
\RequirePackage{graphicx}
\RequirePackage{svg}
\RequirePackage{caption}
\RequirePackage{subcaption}
% == Hyperlinks
\RequirePackage{hyperref}
\RequirePackage{url}
% == Enumeration
\RequirePackage{outlines}
\RequirePackage{enumitem}
% == Tables
\RequirePackage{tabularx}
% == Glossaries
\RequirePackage[acronym, xindy, toc]{glossaries}

% = Variables
\newcommand\@subject{}
\newcommand\subject[1]{\renewcommand\@subject{#1}}

% = Package Configuration
% == Footnotes
\def\arraystretch{1.5}
\renewcommand{\thefootnote}{\Roman{footnote}}
% == Header
\pagestyle{fancy}
\fancyhf{}

\makeatletter
\fancyhead[L]{\small \@subject~\--~\thetitle}
\fancyhead[R]{\small \@date}
\fancyfoot[L]{\small \theauthor}
\fancyfoot[R]{\small \thepage~/~{\pageref*{LastPage}}}
\makeatother

\renewcommand{\footrulewidth}{\headrulewidth}
% == Hyperlinks
\hypersetup{colorlinks=true, linkcolor=MidnightBlue, urlcolor=MidnightBlue, citecolor=MidnightBlue}

% = Makros
% == Title
\makeatletter
\renewcommand{\@maketitle}{
  \let \footnote \thanks~\\
  {\Huge\textbf{\@title}}
  \vspace{0.5em}~\\
  {\footnotesize\@author, \@date}
  \vskip 2em
}
\makeatother
