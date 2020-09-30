\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{miclase}

\LoadClass[12pt]{article}

% \RequierePackageWithOptions[margin=0.7in]{geometry}
% \RequierePackageWithOptions[utf8]{inputenc}
% \RequierePackageWithOptions[spanish]{babel}

\RequirePackage{moresize}[12pt]
\RequirePackage{xcolor}[dvipsnames]
\RequirePackage{titling}
\RequirePackage{helvet}
\RequirePackage{fancyhdr}
\RequirePackage{titlesec}
\RequirePackage{datetime2}[useregional]
% Este paquete sirve para poder incluir 
\RequirePackage{listings}
% Si quieres que tu PDF tenga enlaces clickables para moverte entre referencias manten los siguientes 2 paquetes.
\RequirePackage{hyperref}
\RequirePackage{enumitem}
\RequirePackage{tikz}

\usetikzlibrary{shapes.geometric, arrows}
\tikzstyle{startstop} = [rectangle, rounded corners, minimum width=3cm, minimum height=1cm,text centered, draw=black, fill=gray!30]
\tikzstyle{io} = [trapezium, trapezium left angle=70, trapezium right angle=110, minimum width=3cm, minimum height=1cm, text centered, draw=black, fill=gray!30]
\tikzstyle{process} = [rectangle, minimum width=3cm, minimum height=1cm, text centered, draw=black, fill=gray!30]
\tikzstyle{decision} = [diamond, minimum width=3cm, minimum height=1cm, text centered, draw=black, fill=gray!30]
\tikzstyle{arrow} = [thick,->,>=stealth]

\pagestyle{fancy}
\fancyhf{}

\renewcommand\familydefault{\sfdefault}
\DTMnewdatestyle{iftoday}{%
  \renewcommand*{\DTMdisplaydate}[4]{\DTMmonthname{##2} ##3, ##1}%
  \renewcommand*{\DTMDisplaydate}{\DTMdisplaydate}%
}

\DTMsetdatestyle{iftoday}
\definecolor{gray97}{gray}{.97}
\definecolor{gray75}{gray}{.75}
\definecolor{gray45}{gray}{.45}

\lstset{
  frame=Ltb,
  framerule=0pt,
  aboveskip=0.5cm,
  framextopmargin=3pt,
  framexbottommargin=3pt,
  framexleftmargin=0.4cm,
  framesep=0pt,
  rulesep=.4pt,
  backgroundcolor=\color{gray97},
  rulesepcolor=\color{black},
  stringstyle=\ttfamily,
  showstringspaces=false,
  basicstyle=\small\ttfamily,
  commentstyle=\color{gray45},
  keywordstyle=\bfseries\color{red},
  numbers=left,
  numbersep=15pt,
  numberstyle=\tiny,
  numberfirstline=false,
  breaklines=true
}

\lstnewenvironment{listing}[1][]
{\lstset{#1}\pagebreak[0]}{\pagebreak[0]}

\lstdefinestyle{consola}{
  basicstyle=\scriptsize\bf\ttfamily,
  backgroundcolor=\color{gray75}
}

\lstdefinestyle{C}{language=C}

\def\code#1{\texttt{#1}}

\titleformat{name=\section}[block]
{\Large}
{}
{0pt}
{\colorsection}

\titlespacing*{\section}{0pt}{\baselineskip}{\baselineskip}
\newcommand{\colorsection}[1]{\colorbox{black}{\parbox{\dimexpr\textwidth-2\fboxsep}{\color{white} #1}}}

\titleformat{name=\subsection}[block]
{\normalfont\large\bfseries}
{\thesubsection}
{1em}
{}[{\titlerule[0.8pt]}]

\lhead{{\color{gray}{\footnotesize ISAT \\Nota Metodol\'ogica}}}
\rfoot{\thepage}

\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0.5pt}

% Esta es la definicion de la portada, se le pasan 3 parametros:
% El titulo
% El Cliente
% El autor
\newcommand{\ifportada}[3]{
  \begin{titlepage}
    \thispagestyle{empty}
    \noindent\rule{\textwidth}{5pt}
    \begin{flushright}
      {\HUGE \textbf{Proyecto\\ #1}}\\
    \end{flushright}
    \noindent\rule{\textwidth}{0.5pt}
    \vspace{1in}
    \begin{center}
      {\LARGE Nota Metodol\'ogica}
    \end{center}
    \vspace{1in}
    \begin{flushright}
      {\Large
        Preparado para\\ \textit{#2}\\
        \vspace{0.5in}
        Preparado por\\ \textit{#3}\\
      }
      \vspace{0.5in}
      \textit{\today}\\
    \end{flushright}
  \end{titlepage}
}

\newtheorem{teo}{Teo:}
\newtheorem{lema}[teo]{Lema:}
\newtheorem{prop}[teo]{Prop:}
\newtheorem{corolario}[teo]{Corolario:}

\newenvironment{dem}[1][Dem:]{\begin{trivlist}
\item[\hskip \labelsep {\bfseries #1}]}{\end{trivlist}}
\newenvironment{defi}[1][Def:]{\begin{trivlist}
\item[\hskip \labelsep {\bfseries #1}]}{\end{trivlist}}
\newenvironment{ejem}[1][Ejem:]{\begin{trivlist}
\item[\hskip \labelsep {\bfseries #1}]}{\end{trivlist}}
\newenvironment{nota}[1][Nota:]{\begin{trivlist}
\item[\hskip \labelsep {\bfseries #1}]}{\end{trivlist}}

\newcommand{\qed}{\nobreak \ifvmode \relax \else
      \ifdim\lastskip<1.5em \hskip-\lastskip
      \hskip1.5em plus0em minus0.5em \fi \nobreak
      \vrule height0.75em width0.5em depth0.25em\fi}
      
      