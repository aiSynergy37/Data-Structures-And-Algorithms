#include <stdio.h>

struct Node{
	char data;
	Node *left;
	Node *right;
};

void Inorder(Node *root){
	if (root == NULL){
		return;
	}

	Inorder(root->left);
	printf("%c", root->data);
	Inorder(root->right);
}

