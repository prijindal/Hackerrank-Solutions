Node* Insert(Node *head,int data)
{
    Node *node = new Node();
    node->data = data;
    node->next = head;
    return node;
}
