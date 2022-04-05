class Node {          // Node class
  private:            // Access specifier
    int value;        // Attribute (int variable)
    Node next;        // Attribute (Node variable)
  
  public:
    // Constructor
    Node(int value, Node next)
    {
        this->value = value;
        this->next = next;
    }
  
    // Getter
    int getValue(){
      return value;
    }
   
    Node getNext(){
      return next;
    }
};
