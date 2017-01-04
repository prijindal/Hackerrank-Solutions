Node* InsertNode(Node *head,int data)
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


Node* MergeLists(Node *headA, Node* headB)
{
    Node *temp1 = headA;
    Node *temp2 = headB;
    if(headA == NULL) {
        return headB;
    }
    if(headB == NULL) {
        return headA;
    }
    Node *newHead = NULL;
    while(temp1!=NULL || temp2!=NULL) {
        if(temp1==NULL) {
            newHead = InsertNode(newHead, temp2->data);
            temp2 = temp2->next;
            break;
        }
        if(temp2==NULL) {
            newHead = InsertNode(newHead, temp1->data);
            temp1 = temp1->next;
            break;
        }
        if(temp1->data < temp2->data) {
            newHead = InsertNode(newHead, temp1->data);
            temp1 = temp1->next;
        }
        else {
            newHead = InsertNode(newHead, temp2->data);
            temp2 = temp2->next;
        }
    }
    return newHead;
}
