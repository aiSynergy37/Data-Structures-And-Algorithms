#include <stdio.h>

struct Node{
	char data;
	Node *left;
	Node *right;
};

void Preorder(Node *root){
	if (root == NULL){
		return;
	}

	printf("%c", root->data);
	Preorder(root->left);
	Preorder(root->right);
}

