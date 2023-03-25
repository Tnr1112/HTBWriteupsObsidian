
def get_index_template_mio(machineName,os,authors):
    imageOs = ""
    if os == "Linux":
        imageOs = "![Tux](https://github.com/Tnr1112/HTB-Writeups/blob/main/Machines-Maquinas/common-images/linux.jpg?raw=true)"
    elif os == "Windows":
        imageOs = "![Windows](https://github.com/Tnr1112/HTB-Writeups/blob/main/Machines-Maquinas/common-images/windows.jpg?raw=true)"

    authorName = authors[0].name
    authorId = authors[0].id
    return f'''  
# {machineName} ({os}) {imageOs}  - Español

![]()
Creador de la máquina: **[{authorName}](https://app.hackthebox.com/users/{authorId})**
### Writeup por **Tnr1112**

****

'''
    