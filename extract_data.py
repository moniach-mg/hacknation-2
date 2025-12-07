
categories = {
    'credit-card-number',
    'country',
    'adress',
    'political-view',
    'company',
    'name',
    'city',
    'sex',
    'date',
    'school-name',
    'document-number',
    'address',
    'data',
    'health',
    'sexual-orientation',
    'age',
    'bank-account',
    'surname',
    'ethnicity',
    'phone',
    'street',
    'religion',
    'username',
    'relative',
    'secret',
    'email',
    'pesel',
    'sport',
    'job-title',
    'date-of-birth'
}

anotated_texts = []
with open('./content/data_2.txt', 'r', encoding='utf-8') as f:
    anotated_texts = [line.strip() for line in f.readlines()]

raw_texts = []
with open('./content/data_1.txt', 'r', encoding='utf-8') as f:
    raw_texts = [line.strip() for line in f.readlines()]

texts = zip(anotated_texts, raw_texts)

anotated_chars = '''!"#%&'()*+,-./0123456789:;=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]_`abcdefghijklmnoprstuvwxyz «°²³»ÓóüþĄąćĘęŁłŃńŚśŹźŻżɾ‍‑–—‘’‚“”„… €⃣⏳□○☕♂⛳✅✈✔✨❄❤人住宅私️🌍🌐🌞🌟🌪🌱🌴🌸🌿🍪🍬🍽🎀🎁🎄🎉🎓🎥🎵🏃🐾👀👇👋💐💙💚💡💤💨💪💫💼📅📊📖📚📞📢🔒🔥🔹😂😅😉😊😍😫🙄🚀🚴🛍🛒🛡🤔🤖🧗🧵'''
raw_chars      = '''!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ^_`abcdefghijklmnopqrstuvwxyz| §°²³ÓßñóüýþĄąĆćĘęŁłŃńŚśŹźŻżƒɾ́‍‑–—‘’‚“”„… €⃣⏳□○☕♂⛳✅✈✔✨❄❤️🌍🌐🌞🌟🌪🌱🌴🌸🌿🍪🍬🍽🎀🎁🎄🎉🎓🎥🎵🏃🐾👀👇👋💐💙💚💡💤💨💪💫💼📅📊📖📚📞📢🔒🔥🔹😂😅😉😊😫🙄🚀🚴🛍🛒🛡🤔🤖🧗🧵'''
letters = 'abcdefghijklmnopqrstuvwxyzęóąśłżźćń'

def is_similar(s1, s2):
    # print(f'is_similar({s1}, {s2})')
    i1 = 0
    i2 = 0
    while i1 < len(s1) and i2 < len(s2):
        # print(s1[i1], i1, s2[i2], i2)
        if s1[i1].lower() not in letters:
            i1 += 1
            continue

        if s2[i2].lower() not in letters:
            i2 += 1
            continue

        if s1[i1] == s2[i2]:
            i1 += 1
            i2 += 1
        else:
            return False
    
    return True

for anotated, raw in texts:
    print(anotated)
    print(raw)

    anotated_head = 0
    raw_head = 0

    while True:
        # print(anotated[anotated_head], raw[raw_head])

        if anotated[anotated_head] != '[':
            if anotated[anotated_head] == raw[raw_head]:
                anotated_head += 1
                raw_head += 1
                continue

            if anotated[anotated_head].lower() not in letters + '[]':
                anotated_head += 1
                continue

            if raw[raw_head].lower() not in letters:
                raw_head += 1
                continue
        
        if anotated[anotated_head] != '[':
            raise Exception(f'NO \nanotated: "{anotated[anotated_head-10:anotated_head+1]}"\nraw:     "{raw[raw_head-10:raw_head+1]}"')

        # print('inside anotation')

        # advance anotated head until end
        anotation_start = anotated_head
        raw_start = raw_head
        inside_bracket = True
        while inside_bracket:
            anotated_head += 1

            # if encountered a closed bracket
            if anotated[anotated_head] == ']':
                # check if another open bracket is within 2 characters from here (merge consecutive anotations)
                inside_bracket = '[' in anotated[anotated_head:anotated_head+3]
        
        anotated_head += 1
        anotation_end = anotated_head
        while anotated[anotated_head] == ' ':
            anotated_head += 1

        # the anotated head is now outside the anotation
        next_anotation = anotated[anotated_head:].find('[') + anotated_head
        # print("anotation_start:", anotation_start)
        # print("anotation_end:", anotation_end)
        # print("anotated_head:", anotated_head)
        # print("next_anotation:", next_anotation)
        if next_anotation == -1:
            break
        span = next_anotation - anotated_head
        # print("span:", span)
        raw_end = raw_head
        similar = False
        while not similar:
            similar = is_similar(anotated[anotated_head:next_anotation], raw[raw_end:raw_end+min(10, span)])
            raw_end += 1
            if similar:
                while anotated[anotated_head] != raw[raw_end]:
                    raw_end += 1

        anotation = anotated[anotation_start:anotation_end]
        raw_section = raw[raw_start:raw_end]
        raw_head = raw_end

        print(anotation, '->', raw_section)

        # print("anotation_start:", anotation_start)
        # print("anotation_end:", anotation_end)
        # print("anotated_head:", anotated_head)
        # print("raw_start:", raw_start)
        # print("raw_end:", raw_end)
        # print("raw_head:", raw_head)
        # print(f'anotated: "{anotated[anotated_head-10:anotated_head]}"\nraw:     "{raw[raw_head-10:raw_head]}"')


    break