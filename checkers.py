import pygame
import sys

# Initialize pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# RGB colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# Create the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

# Load assets for pieces (optional)
CROWN = pygame.transform.scale(pygame.image.load('crown.png'), (44, 25))

# Main function to run the game
def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    selected_piece = None

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                if selected_piece:
                    move = board.move(selected_piece, row, col)
                    if not move:
                        selected_piece = None
                else:
                    selected_piece = board.select_piece(row, col)

        board.draw(WIN)
        pygame.display.update()

    pygame.quit()
    sys.exit()

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# Function to draw the board
def draw_board(win):
    win.fill(BLACK)
    for row in range(ROWS):
        for col in range(row % 2, COLS, 2):
            pygame.draw.rect(win, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Class to handle individual pieces
class Piece:
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

# Class to handle the board and game logic
class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.create_board()

    def create_board(self):
        for row in range(ROWS):
            self.board.append([0] * COLS)

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, RED, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def select_piece(self, row, col):
        piece = self.board[row][col]
        if piece != 0:
            self.selected_piece = piece
            return piece
        return None

    def move(self, piece, row, col):
        if self.valid_move(piece, row, col):
            self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
            piece.move(row, col)
            return True
        return False

    def valid_move(self, piece, row, col):
        if self.board[row][col] != 0:  # Destination square must be empty
            return False

        dx = abs(piece.row - row)
        dy = abs(piece.col - col)

        if dx == 1 and dy == 1:  # Ensure the piece moves only one square diagonally
            return True

        return False

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

# Run the game
if __name__ == "__main__":
    main()
