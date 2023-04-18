function findOneRectangle(board) {
    if (!board || board.length === 0 || board[0].length === 0) {
      return [];
    }
    const result = [];
    for (let i = 0; i < board.length; i++) {
      for (let j = 0; j < board[0].length; j++) {
        if (board[i][j] === 0) {
          result.push([i, j]);
          let height = 1, width = 1;
          while (i + height < board.length && board[i + height][j] === 0) {
            height++;
          }
          while (j + width < board[0].length && board[i][j + width] === 0) {
            width++;
          }
          result.push([i + height - 1, j + width - 1]);
          break;
        }
        if (result.length !== 0) {
          break;
        }
      }
    }
    return result;
}




board = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1],
    [5, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
];

console.log(findOneRectangle(board))