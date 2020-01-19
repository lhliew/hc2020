from sentence_comparison import preprocessing, comparison

def build_html_string(written, spoken):
    written_og = written.split()
    print(spoken)
    written_after_preprocesssing = preprocessing(written).split()
    words_matched = comparison(written, spoken)[1]

    # print('original length = ', len(written_og), " length after preprocessing = ", len(written_after_preprocesssing))
    print(written_og)
    print(written_after_preprocesssing)
    print(words_matched)
    words_matched.append("END")

    html_string = ["<h1 style='color:lawngreen;font-size:40px'>"]

    for i in range(len(written_after_preprocesssing)):
        # if len(words_matched) == 0:
        #     # html_string.append("<span style='color:red'>")
        #     # html_string.append(written_og[i])
        #     # html_string.append("</span>")
        #     break

        if (written_after_preprocesssing[i] == words_matched[0]):
            html_string.append(written_og[i])
            del words_matched[0]
        else:
            html_string.append("<span style='color:red'>")
            html_string.append(written_og[i])
            html_string.append("</span>")
    html_string.append("</h1>")
    html_string = " ".join(html_string)

    print(html_string)
    return html_string

def build_spoken_html(spoken):
    html_string = ["<h1 style='color:white;font-size:30px'>"]
    # print(spoken)
    spoken = spoken.split()
    # print(spoken)
    for word in spoken:
        html_string.append(word)
    html_string.append("</h1>")
    html_string = " ".join(html_string)
    print(spoken)
    print(html_string)

    return html_string
# written = "The cat is sitting."
# spoken = "cat his sitting"

# print(build_html_string(written, spoken))
