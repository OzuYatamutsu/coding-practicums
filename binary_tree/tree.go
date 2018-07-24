package binary_tree
import "fmt"

type Tree struct {
    left *Tree
    right *Tree
    value *int
}

func New() *Tree {
    return &Tree{}
}

func (tree *Tree) Add(value int) {
    if tree.value == nil {
        tree.value = &value
        return
    }

    if value < *tree.value {
        if tree.left != nil {
            tree.left.Add(value)
        } else {
            tree.left = &Tree{nil, nil, &value}
        }
    }

    if value >= *tree.value {
        if tree.right != nil {
            tree.right.Add(value)
        } else {
            tree.right = &Tree{nil, nil, &value}
        }
    }
}

func (tree *Tree) InOrderTraversal() {
    fmt.Printf("%d ", *tree.value)
    if tree.left != nil {
        tree.left.InOrderTraversal()
    }
    if tree.right != nil {
        tree.right.InOrderTraversal()
    }
}
