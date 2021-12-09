#include <bits/stdc++.h>

using namespace std;

int max(int x, int y){
    return (x > y)? x:y;
}

class node{
    public:
    int data;
    node *left, *right;
};

int LISS(node *root){
    if(root == NULL){
        return 0;
    }

    int size_execluded = LISS(root->left)+LISS(root->right);
    int size_included = 1;
    if(root->left){
        size_included+=LISS(root->left->left)+LISS(root->left->right);
    }

    if(root->right){
        size_included+=LISS(root->right->left)+LISS(root->right->right);
    }

    return max(size_included, size_execluded);
}

node * newNode(int data){
    node *temp = new node();
    temp-> data = data;
    temp->left = temp->right = NULL;
    return temp;
}

int main()
{
    // Let us construct the tree
    // given in the above diagram
    node *root = newNode(20);
    root->left = newNode(8);
    root->left->left = newNode(4);
    root->left->right = newNode(12);
    root->left->right->left = newNode(10);
    root->left->right->right = newNode(14);
    root->right = newNode(22);
    root->right->right = newNode(25);
 
    cout << "Size of the Largest"
         << " Independent Set is "
         << LISS(root);
 
    return 0;
}
