import marshal
import zlib
import base64
import random
import sys
MINZ_CHARS = ['A҉҈⃟⃠꙰꙲⃝⃞⃤', '1҉҈⃟⃠꙰꙲⃝⃞⃤', '★҉҈⃟⃠꙰꙲⃝⃞⃤', '☠҉҈⃟⃠꙰꙲⃝⃞⃤', '☣҉҈⃟⃠꙰꙲⃝⃞⃤', '▓҉҈⃟⃠꙰꙲⃝⃞⃤', '▒҉҈⃟⃠꙰꙲⃝⃞⃤', '░҉҈⃟⃠꙰꙲⃝⃞⃤', '█҉҈⃟⃠꙰꙲⃝⃞⃤', '✦҉҈⃟⃠꙰꙲⃝⃞⃤']
def make_it_cursed(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            source_code = f.read()
        code_obj = compile(source_code, '<minz>', 'exec')
        compressed = zlib.compress(marshal.dumps(code_obj))
        encoded = base64.b64encode(compressed).decode('utf-8')
        unique_chars = sorted(list(set(encoded)))
        char_map = {}
        glitch_alphabet = []
        base_minz_len = len(MINZ_CHARS)
        for i, char in enumerate(unique_chars):
            p1 = MINZ_CHARS[i % base_minz_len]
            p2 = MINZ_CHARS[(i + 1) % base_minz_len]
            minz_symbol = f'{p1}{p2}{i}҉҈⃟⃠꙰꙲⃝⃞⃤'
            char_map[char] = minz_symbol
            glitch_alphabet.append(minz_symbol)
        cursed_payload = ''.join([char_map[c] for c in encoded])
        reverse_map = {v: k for k, v in char_map.items()}
        header = '#⚠️ TOOLS OBFUSCATOR ⚠️\n#□MINZX TOOLS□\n\n'
        payload_var = f'_ = \"{cursed_payload}\"'
        dict_str = str(reverse_map)
        loader_script = f'\nimport marshal, zlib, base64\nd={dict_str}\np=_\no=\"\"\n# Loop pemecah simbol\nwhile p:\n for k,v in d.items():\n  if p.startswith(k):\n   o+=v;p=p[len(k):];break\nexec(marshal.loads(zlib.decompress(base64.b64decode(o))))\n'
        loader_hex = loader_script.encode('utf-8').hex()
        final_exec = f'exec(bytes.fromhex(\'{loader_hex}\').decode(\'utf-8\'))'
        final_content = f'{header}{payload_var}\n{final_exec}'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f'[SUCCESS] MINZ OBFUSCATOR CREATED: {output_file}')
        print('Thx for using this script, by @MinzXitV.')
    except Exception as e:
        print(f'[ERROR] {e}')
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python minzobf.py <target.py>')
    else:
        make_it_cursed(sys.argv[1], 'minz_' + sys.argv[1])