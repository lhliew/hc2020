from sentence_comparison import preprocessing, comparison

def build_html_string(written, spoken):
    written_og = written.split()
    written_after_preprocesssing = preprocessing(written).split()
    words_matched = comparison(written, spoken)[1]

    # print('original length = ', len(written_og), " length after preprocessing = ", len(written_after_preprocesssing))

    html_string = ["<h1 style='colour:green'>"]
    for i in range(len(written_after_preprocesssing)):
        if (written_after_preprocesssing[i] == words_matched[0]):
            html_string.append(written_og[i])
            del words_matched[0]
        else:
            html_string.append("<span style='colour:red'>")
            html_string.append(written_og[i])
            html_string.append("</span>")
    html_string.append("</h1>")
    html_string = " ".join(html_string)

    return html_string


# written = "The cat is sitting."
# spoken = "cat his sitting"

# print(build_html_string(written, spoken))