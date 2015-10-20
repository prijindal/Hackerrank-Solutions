Node* InsertNth(Node *head, int data, int position)
{
    Node *node = new Node();
    node->data = data;
    if(head == NULL) {
        node->next = NULL;
        return node;
    }
    if (position == 0) {
        node->next = head;
        return node;
    }
    int i = 0;
    Node *temp = head;
    while(i < position - 1 && temp->next == NULL) {
        temp = temp->next;
        i++;
    }
    Node *temp1 = temp;
    node->next = temp1->next;
    temp1->next = node;
    return head;
}
