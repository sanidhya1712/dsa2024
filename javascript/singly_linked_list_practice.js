class Node {
    constructor(value) {
        this.value = value
        this.next = null
    }
}

class LinkedList {
    constructor() {
        this.head = null
        this.tail = null
        this.size = 0
    }
    addAtHead(value) {
        let node = new Node(value)
        if (!this.head) {
            this.head = node
            this.tail = node
        } else {
            node.next = this.head
            this.head = node
        }
        this.size++
        return this
    }
    getList() {
        let i = 0
        let node = this.head
        while (i < this.size) {
            console.log(node.value, " --> ");
            node = node.next
            i++
        }
    }
    get() {

    }
    addAtTail() {

    }
    addAtIndex() {

    }
    deleteAtIndex() {

    }
}

s = new LinkedList()
s.addAtHead(3)
s.addAtHead(12)
s.addAtHead(11)
s.getList()