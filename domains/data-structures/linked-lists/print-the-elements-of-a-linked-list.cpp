void Print(Node *head) {
    Node *temp;
    temp = head;
    while(temp!=NULL) {
        cout<<temp->data<<'\n';
        temp = temp->next;
    }
}
