
def operator(stack,token,precedence,postfix_list):
    while (stack and stack[-1]!='(' and
           (precedence[stack[-1]] > precedence[token] or
            (precedence[stack[-1]] == precedence[token] and token != '^'))):
        postfix_list.append(stack.pop())
    stack.append(token)

infix_exp=input("Enter the infix expression: ")
stack=[]
postfix_list=[]
infix_list=list(infix_exp)
precedence={'^':3,'*':2,'/':2,'+':1,'-':1}
for token in infix_list:
    #print(token,stack,postfix_list)
    if token in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
        postfix_list.append(token)
    elif token=='(':
        stack.append(token)
    elif token==")":
        top_token = stack.pop()
        while top_token != "(":
            postfix_list.append(top_token)
            top_token = stack.pop()
    else:
        if token in precedence:
            if len(stack)==0 or stack[-1]=='(':
                stack.append(token)
            elif stack[-1] in precedence:
                operator(stack,token,precedence,postfix_list)

while stack:
    postfix_list.append(stack.pop())
print("Postfix Expression: ", ''.join(postfix_list))

