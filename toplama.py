def toplama(n):
    A=n.split("+")
    cem=0
    for i in A:
        try:
            cem=cem+float(i)
        except (ValueError, TypeError):
            cem=cem+cixma(i)
    return cem
def cixma(n):
    A=n.split("-")
    try:
        ferq=float(A[0])
    except (ValueError, TypeError):
        ferq=vurma(A[0])
    for i in range(1, len(A)):
        try:
            ferq=ferq-float(A[i])
        except (ValueError, TypeError):
            ferq=ferq-vurma(A[i])
    return ferq
def vurma(n):
    A=n.split("*")
    hasil=1
    for i in A:
        try:
            hasil=hasil*float(i)
        except (ValueError, TypeError):
            hasil=hasil*bolme(i)
    return hasil      
def bolme(n):
    A=n.split("/")
    try:
        qismet=float(A[0])
    except (ValueError, TypeError):
        xeta()
    for i in range(1, len(A)):
        try:
            qismet=qismet/float(A[i])
        except (ValueError, TypeError):
            qismet=0
    return qismet
def xeta():
    print("xeta")
