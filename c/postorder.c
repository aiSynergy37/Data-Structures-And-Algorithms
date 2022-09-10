#include <stdio.h>

struct Node{
	char data;
	Node *left;
	Node *right;
};

void Postorder(Node *root){
	if (root == NULL){
		return;
	}

	Postorder(root->left);
	Postorder(root->right);
	printf("%c ", root->data);
}

