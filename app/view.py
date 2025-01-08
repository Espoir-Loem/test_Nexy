# coding: jsx
from pyjsx import jsx, JSX


def Header(children, style=None, **rest) -> JSX:
    return <h1 style={style}>{children}</h1>


def Main(children, **rest) -> JSX:
    return <main>{children}</main>


def sya():
    print("hemmp")

def App() -> JSX:
    name = 8
    return (
        <div class="bg-red-200 h-dvh p-10 space-y-1">
            <link rel="stylesheet" href="/public/assets/css/main.css"/>
            <Header style={{"color": "red"}}>Hello, world!</Header>
            <Main>
                <p >This was rendered with PyJSX!</p>
                {
                <span>bonjour</span> if name > 6 
                else <span>bonjour je suis là</span>
                }
                <button lass="cursor-pointer ">
                    <img src="/public/a.png" class="w-[70vw] rounded-2xl border-2 border-red-400"/>
                </button>
                { "espoir".upper()}
               <div>
                je suis entrain de travailler
               </div>
            </Main>
        </div>
    )
