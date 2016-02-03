let finalSquare = 30
var board = [Int](count: finalSquare + 1, repeatedValue: 0)

board[03] = +08; board[06] = +11; board[09] = +09; board[10] = +02
board[14] = -10; board[19] = -11; board[22] = -02; board[24] = -08

var square = 0
var diceRoll = 0

gameLoop: while square != finalSquare {
    if ++diceRoll == 7 { diceRoll = 1 }
    switch square + diceRoll {
      case finalSquare:
        // diceRoll will move us to the final square, so the game is over
        break gameLoop
      case let newSquare where newSquare > finalSquare:
        // diceRoll will move us beyond the final square, so roll again
        continue gameLoop
      default:
        // this is a valid move, so find out its effect
        square += diceRoll
        square += board[square]
    }
    
    print(diceRoll, "/", square)
}
print("Game over!")