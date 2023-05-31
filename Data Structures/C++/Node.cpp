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
    int GetValue(){
      return value;
    }
   
    Node GetNext(){
      return next;
    }
};
