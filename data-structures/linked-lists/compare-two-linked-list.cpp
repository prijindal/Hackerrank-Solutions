int CompareLists(Node *headA, Node* headB)
{
    Node *temp1 = headA;
    Node *temp2 = headB;
    while(temp1!=NULL&&temp2!=NULL) {
        if(temp1->data!=temp2->data) {
            return false;
        }
        temp1 = temp1->next;
        temp2 = temp2->next;
    }
    if(temp1!=NULL || temp2!=NULL) {
        return false;
    }
    return true;
}
