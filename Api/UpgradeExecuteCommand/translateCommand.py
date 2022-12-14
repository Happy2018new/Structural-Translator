class UnknownCommand(Exception):
    def __init__(self,value:str):
        Exception.__init__(self, f'Unknown command {value}')

class SyntaxError(Exception):
    def __init__(self, value:list):
        Exception.__init__(self, f'Incorrect position ({value[0]},{value[1]},{value[2]})')

class ErrorSelector(Exception):
    def __init__(self, command:str, pointer:int):
        Exception.__init__(self, f'Incorrect selector >>>{command[pointer:pointer+5]}<<<')

class BrokenPos(Exception):
    def __init__(self, command:str, pointer:int):
        Exception.__init__(self, f'Incorrect position >>>{command[pointer:pointer+5]}<<<')

class ErrorDetect(Exception):
    def __init__(self, command:str, pointer:int):
        Exception.__init__(self, f'Incorrect detect value >>>{command[pointer:pointer+5]}<<<')





def jumpSpace(command:str,pointer:int)->int:
    while True:
        if pointer >= len(command) - 1:
            return pointer
        elif command[pointer] == ' ' or command[pointer] == '/':
            pointer = pointer + 1
        else:
            return pointer





def highSearching(command:str,pointer:int,input:list)->list:
    List = [[command.find(i,pointer),len(i)] for i in input]
    ans = []
    for i in List:
        if i[0] != -1:
            ans.append(i)
    ans.sort()
    return [
        ans[0][0],
        ans[0][1]
    ]





def getRightBarrier(command:str,pointer:int)->int:
    while True:
        quotationMark = command.find('"',pointer)
        barrier = command.index(']',pointer)
        if quotationMark == -1:
            return barrier
        elif quotationMark < barrier:
            pointer = command.find('"',quotationMark+1) + 1
        else:
            return barrier





def searchForExecute(command:str,pointer:int)->list:
    pointer = jumpSpace(command,pointer)

    if command[pointer:pointer+7].lower() == 'execute':
        return [pointer+7,True]

    if command[pointer:pointer+5].lower() == 'align':
        raise UnknownCommand('align')
    if command[pointer:pointer+8].lower() == 'anchored':
        raise UnknownCommand('anchored')
    if command[pointer:pointer+2].lower() == 'as':
        raise UnknownCommand('as')
    if command[pointer:pointer+2].lower() == 'at':
        raise UnknownCommand('at')
    if command[pointer:pointer+6].lower() == 'facing':
        raise UnknownCommand('facing')
    if command[pointer:pointer+2].lower() == 'in':
        raise UnknownCommand('in')
    if command[pointer:pointer+10].lower() == 'positioned':
        raise UnknownCommand('positioned')
    if command[pointer:pointer+7].lower() == 'rotated':
        raise UnknownCommand('rotated')
    
    if command[pointer:pointer+2].lower() == 'if':
        raise UnknownCommand('if')
    if command[pointer:pointer+6].lower() == 'unless':
        raise UnknownCommand('unless')

    if command[pointer:pointer+3].lower() == 'run':
        raise UnknownCommand('run')

    return [pointer,False]





def getSelector(command:str,pointer:int)->list:
    pointer = jumpSpace(command,pointer)
    if command[pointer] == '@':
        transit = highSearching(command,pointer,['@s','@a','@p','@e','@r','@initiator','@c','@v'])
        selector = command[
            pointer:
            transit[0] + transit[1]
        ]
        pointer = jumpSpace(command,transit[0] + transit[1])
        if pointer >= len(command) - 1:
            return [selector,pointer]
        elif command[pointer] != '[':
            return [selector,pointer]
        else:
            transit = getRightBarrier(command,pointer)
            return [
                selector + command[
                    pointer:
                    transit + 1
                ],
                transit + 1
            ]
    elif command[pointer] == '"':
        transit = command.index('"',pointer + 1)
        return [
            command[pointer:transit + 1],
            transit + 1
        ]
    else:
        transit = highSearching(command,pointer,[' ','^','~'])
        return [
            command[
                pointer:
                transit[0] + transit[1] - 1
            ],
            transit[0] + transit[1] - 1
        ]





def getPos(command:str,pointer:int)->list:
    pointer = jumpSpace(command,pointer)
    ans = []
    for i in range(3):
        transit = highSearching(command,pointer+1,[' ','^','~','a','b','c','d','e','f','g','h','i','j','k','l','m','n',
        'o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
        'P','Q','R','S','T','U','V','W','X','Y','Z','?','/'])

        successStates = False
        for i in ['^','~','-','0','1','2','3','4','5','6','7','8','9']:
            if command[pointer] == i:
                successStates = True

        if successStates == False:
            raise BrokenPos(command,pointer)

        ans.append(
            command[
                pointer:
                transit[0]
            ])
        pointer = jumpSpace(command,transit[0])

    for i in range(len(ans)):
        if ans[i][0] == '^' or ans[i][0] == '~':
            save = ans[i]
            ans[i] = ans[i][1:]
            if ans[i] != '':
                ans[i] = str(float(ans[i]) if float(ans[i]) != int(float(ans[i])) else int(float(ans[i])))
                if ans[i] == '0':
                    ans[i] = ''
            ans[i] = '^' + ans[i] if save[0] == '^' else '~' + ans[i]
        else:
            if ans[i].find('.') != -1:
                ans[i] = str(float(float(ans[i]) if float(ans[i]) != int(float(ans[i])) else int(float(ans[i]))))
            else:
                ans[i] = str(float(ans[i]) if float(ans[i]) != int(float(ans[i])) else int(float(ans[i])))

    if ans[0][0] == "^" or ans[1][0] == "^" or ans[2][0] == "^":
        if ans[0][0] != "^" or ans[1][0] != "^" or ans[2][0] != "^":
            raise SyntaxError(ans)

    return [
        ans[0] + ' ' + ans[1] + ' ' + ans[2],
        pointer
    ]





def detectBlock(command:str,pointer:int)->list:
    pointer = jumpSpace(command,pointer)
    if command[pointer:pointer+6].lower() == 'detect':
        pointer = getPos(command,jumpSpace(command,pointer+6))
        pos = pointer[0]
        startLocation = pointer = jumpSpace(command,pointer[-1])
        endLocation = command.index(' ',pointer)
        spaceLocation = command.index(' ',jumpSpace(command,endLocation + 1))
        return [
            True,
            f' if block {pos} {command[startLocation:endLocation]} {command[endLocation + 1:spaceLocation]}',
            spaceLocation
        ]
    else:
        return [
            False,
            pointer
        ]





def run(command:str)->str:
    ans = []
    pointer = -1



    while True:
        pointer = pointer + 1
        markable = searchForExecute(command,pointer)


        if markable[1] == True:
            try:
                selector = getSelector(command,markable[0])
            except:
                raise ErrorSelector(command,pointer)

            try:
                pos = getPos(command,selector[-1])
            except:
                raise BrokenPos(command,selector[-1])

            try:
                detect = detectBlock(command,pos[-1])
            except:
                raise ErrorDetect(command,pos[-1])

            pointer = detect[-1] - 1

            selector = selector[0]
            pos = pos[0]
            detect = detect[1] if detect[0] == True else ''

            ans.append(
                f'as {selector} at @s{detect} ' if (
                    pos == '~ ~ ~') or (pos == '^ ^ ^') 
                    else f'as {selector} at @s positioned {pos}{detect} '
            )
        else:
            ans.append(command[markable[0]:])
            break


    if len(ans) <= 1:
        return "".join(ans)
    else:
        ans[-1] = 'run ' + ans[-1]
        return 'execute ' + "".join(ans)