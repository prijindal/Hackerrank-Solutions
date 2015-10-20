Node* Insert(Node *head,int data)
{
    if(head == NULL){
        Node *head1 = new Node();
        head = head1;
        head->data = data;
        head->next = NULL;
        return head;
    }
    else {
        Node *node = new Node(); 
        Node *temp = head;
        while(temp->next!=NULL) {
            temp = temp->next;
        }
        node->data = data;
        node->next = NULL;
        temp->next = node;
        return head;
    }
}
