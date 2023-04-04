from sentence_transformers import SentenceTransformer, util
import ocr

image_arr = ocr.image_get()
generated_text = ocr.image_load_converter(image_arr)
print(generated_text)

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
model.max_seq_length = 256

#generated_text = 'Oli- Data warehouse was the turn givenAnd by Bill Inman in 1950,# A subject oriented, Integrated, timeGovernment and Non-vocative Collection.'
ans = 'A data warehouse is subject oriented, time Variant, non - volatile, and integrated. Coined by Bill Inman.'
sentences = [generated_text, ans]

embeddings = model.encode(sentences, normalize_embeddings=True)
dot_score = util.dot_score(embeddings[0], embeddings[1])
score = dot_score.item()*100
print(f"The answer is:{score: .2f}% similar")

def calc_marks(score):
  marks = 0
  if (score < 45):
    pass
  elif (score >= 45 and score < 50):
    marks += 1
  elif (score >= 50 and score < 60):
    marks += 2
  elif (score >= 60 and score < 70):
    marks += 3
  elif (score >= 70 and score < 80):
    marks += 4
  else:
    marks += 5
  return marks

marks_of_student_in_ans1 = calc_marks(score)
print(f"Marks: {marks_of_student_in_ans1}/5")