import ast, sys

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'in'
    source = open(path).read()
    source = source.translate(str.maketrans('+*', '*+'))
    tree = ast.parse(source)
    traverse(tree)
    res = 0
    for expr in tree.body:
        val = eval(compile(ast.Expression(expr.value), 'N/A', 'eval'))
        res += val
    print(res)

def traverse(node):
    if isinstance(node, ast.Module):
        for child in node.body:
            traverse(child)
    elif isinstance(node, ast.Expr):
        traverse(node.value)
    elif isinstance(node, ast.BinOp):
        visit(node)
        traverse(node.left)
        traverse(node.right)

def visit(binop_node):
    if isinstance(binop_node.op, ast.Add):
        binop_node.op = ast.Mult()
    elif isinstance(binop_node.op, ast.Mult):
        binop_node.op = ast.Add()
    else:
        1/0


main()
