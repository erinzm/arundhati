chosen_words = [];

$('span.word').click(function() {
  let word = $(this).attr('data-word');
  let idxof = chosen_words.indexOf(word);
  if (idxof == -1 ) {
    chosen_words.push(word);
    $(this).addClass('picked');
  } else {
    chosen_words.splice(idxof, 1);
    $(this).removeClass('picked');
  }
});

$('button#relevant').click(function() {
  submitAnswer(1, chosen_words);
});

$('button#irrelevant').click(function() {
  submitAnswer(-1, chosen_words);
});

function submitAnswer(reward, relevant_words) {
}
