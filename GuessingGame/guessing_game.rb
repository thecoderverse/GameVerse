class GuessingGame
  def initialize
    @min_number = 1
    @max_number = 10
    @number = rand(@min_number..@max_number)
    @guesses_left = 3
    @level = 1
  end

  def play
    loop do
      print "Guess a number between #{@min_number} and #{@max_number} (#{@guesses_left} guesses left, level #{@level}): "
      guess = gets.chomp.to_i
      @guesses_left -= 1

      if guess == @number
        puts "Congratulations, you guessed the number in #{3 - @guesses_left} guesses! Moving to level #{@level + 1}..."
        @level += 1
        @guesses_left = 3
        @min_number = 1
        @max_number = 10 * @level
        @number = rand(@min_number..@max_number)
      elsif guess < @number
        puts "The number is higher than #{guess}."
        puts "Hint: The number is between #{guess} and #{@max_number}" if @guesses_left > 0
        @min_number = guess + 1
      else
        puts "The number is lower than #{guess}."
        puts "Hint: The number is between #{@min_number} and #{guess}" if @guesses_left > 0
        @max_number = guess - 1
      end

      if @guesses_left == 0
        puts "Sorry, you didn't guess the number. The correct number was #{@number}."
        break
      end
    end
  end
end

game = GuessingGame.new
game.play
