Node* Delete(Node *head, int position)
{
    Node *temp = head;
    int i = 0;
    if(position == 0) {
        return head->next;
    }
    while(temp->next!=NULL && i < position - 1) {
        temp = temp->next;
        i++;
    }
    if(temp->next==NULL) {
        temp=NULL;
        return head;
    }
    Node *temp1 = temp->next;
    temp->next = temp1->next;
    return head;
}
