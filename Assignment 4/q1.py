# Question 1: Spotify Playlist Shuffle Detection (Cycle Detection in Linked List)
# Please DO NOT modify the given code except the TODO part
# You may add your own helper functions if necessary


class ListNode:
    """A node in a singly linked list representing a song in playlist."""
    def __init__(self, song_name):
        self.song = song_name
        self.next = None


def create_playlist(songs, cycle_index=-1):
    """
    Helper function: Create a playlist (linked list) from a list of song names.

    parameter songs: list of strings (song names)
    parameter cycle_index: if >= 0, the last node will point to the node at this index
                          creating a cycle. If -1, no cycle is created.
    return: head node of the playlist
    """
    if not songs:
        return None

    head = ListNode(songs[0])
    current = head
    nodes = [head]

    for song in songs[1:]:
        current.next = ListNode(song)
        current = current.next
        nodes.append(current)

    # Create cycle if specified
    if cycle_index >= 0 and cycle_index < len(nodes):
        current.next = nodes[cycle_index]

    return head


def print_playlist(head, max_print=10):
    """
    Helper function: Print the playlist (with cycle protection).

    parameter head: head node of the playlist
    parameter max_print: maximum number of songs to print (to avoid infinite loop)
    return: None
    """
    current = head
    count = 0
    songs = []
    while current and count < max_print:
        songs.append(current.song)
        current = current.next
        count += 1

    if current:
        print(songs, "... (cycle detected, stopping print)")
    else:
        print(songs)


def has_cycle(head):
    """
    Detect if the playlist contains a cycle using Floyd's algorithm.

    Use the Tortoise and Hare approach:
    - Slow pointer moves 1 step at a time
    - Fast pointer moves 2 steps at a time
    - If they meet, there's a cycle

    parameter head: ListNode, the head of the playlist
    return: bool, True if cycle exists, False otherwise

    Example:
        Playlist: A -> B -> C -> D -> B (cycle back to B)
        Returns: True

        Playlist: A -> B -> C -> None
        Returns: False
    """
    # TODO part
    # ------- Your code start here -------



    # ------- End of your code -----------


def find_cycle_start(head):
    """
    Find the node where the cycle begins using Floyd's algorithm.

    After detecting a cycle (slow and fast meet):
    - Reset one pointer to head
    - Move both pointers 1 step at a time
    - They will meet at the cycle start

    parameter head: ListNode, the head of the playlist
    return: ListNode, the node where cycle starts, or None if no cycle

    Example:
        Playlist: A -> B -> C -> D -> B (cycle back to B)
        Returns: Node containing "B"

        Playlist: A -> B -> C -> None
        Returns: None
    """
    # TODO part
    # ------- Your code start here -------



    # ------- End of your code -----------


# Test cases
if __name__ == '__main__':
    print("=" * 50)
    print("Test Case 1: Playlist with cycle")
    print("=" * 50)
    # Create: "Mo Bai" -> "Erta" -> "Mo Wen" -> "Shi Jie" -> back to "Erta"
    playlist1 = create_playlist(["Mo Bai", "Erta", "Mo Wen", "Shi Jie"], cycle_index=1)
    print("Playlist (with cycle at index 1):")
    print_playlist(playlist1)
    print(f"has_cycle: {has_cycle(playlist1)}")  # Expected: True
    cycle_node = find_cycle_start(playlist1)
    print(f"Cycle starts at: {cycle_node.song if cycle_node else None}")  # Expected: Erta
    print()

    print("=" * 50)
    print("Test Case 2: Normal playlist (no cycle)")
    print("=" * 50)
    playlist2 = create_playlist(["Hello", "Goodbye", "Yesterday", "Let It Be"])
    print("Playlist (no cycle):")
    print_playlist(playlist2)
    print(f"has_cycle: {has_cycle(playlist2)}")  # Expected: False
    cycle_node2 = find_cycle_start(playlist2)
    print(f"Cycle starts at: {cycle_node2.song if cycle_node2 else None}")  # Expected: None
    print()

    print("=" * 50)
    print("Test Case 3: Single song looping to itself")
    print("=" * 50)
    playlist3 = create_playlist(["On Repeat"], cycle_index=0)
    print("Playlist (single song cycle):")
    print_playlist(playlist3)
    print(f"has_cycle: {has_cycle(playlist3)}")  # Expected: True
    cycle_node3 = find_cycle_start(playlist3)
    print(f"Cycle starts at: {cycle_node3.song if cycle_node3 else None}")  # Expected: On Repeat
    print()

    print("=" * 50)
    print("Test Case 4: Empty playlist")
    print("=" * 50)
    playlist4 = create_playlist([])
    print("Playlist (empty):")
    print_playlist(playlist4)
    print(f"has_cycle: {has_cycle(playlist4)}")  # Expected: False
    cycle_node4 = find_cycle_start(playlist4)
    print(f"Cycle starts at: {cycle_node4}")  # Expected: None
    print()

    print("=" * 50)
    print("Test Case 5: Cycle at the end pointing to head")
    print("=" * 50)
    playlist5 = create_playlist(["Start", "Middle", "End"], cycle_index=0)
    print("Playlist (cycle back to head):")
    print_playlist(playlist5)
    print(f"has_cycle: {has_cycle(playlist5)}")  # Expected: True
    cycle_node5 = find_cycle_start(playlist5)
    print(f"Cycle starts at: {cycle_node5.song if cycle_node5 else None}")  # Expected: Start