package main
import "./binary_tree"


func main() {
    tree := binary_tree.New()
    tree.Add(1)
    tree.Add(2)
    tree.Add(3)
    tree.Add(4)
    tree.InOrderTraversal()
}

