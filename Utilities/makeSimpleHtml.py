#!/usr/bin/env python
import glob
import imghdr
import argparse

def writeHTML(path, name):
    image_files = [x for x in glob.glob(path + "/plots/*.*") if imghdr.what(x)]
    with open('%s/index.html' % path, 'w') as index:
        index = open('%s/index.html' % path, 'w')
        index.write('<html>\n'
            '<head>\n'
            '  <title>{title}</title>\n'
            '  <style type="text/css">\n'
            '    .autoResizeImage {{\n'
            '      max-width: 100%;\n'
            '      height: auto;\n'
            '      width: auto;\n'
            '   }}\n'
            '   </style>\n'
            '</head>\n'
            '<body>\n'.format(title=name)
        )
        index.write('  <div style="text-align: center;"><b>{title}</b></div>\n'
                '  <table>\n'.format(title=name)
        )
        for i, image_file in enumerate(image_files):
            file_name = image_file.strip().split('/')[-1].strip() 
            if i % 3 == 0: 
                index.write('  <tr style="text-align: center;">\n')
            index.write(getTableRow(image_file.split("/")[-1]))
            if (i+1) % 3 == 0: 
                index.write('  </tr>\n')
        index.write( '</body>\n'
                '</html>' )
def getTableRow(image_file):
    return '''    <td style="text-align: center;">
        <img src="plots/{image}" class="autoResizeImage" /><br/>
        <a href="logs/{name}_event_info.log">[log]</a> - 
        <a href="logs/{name}_event_info-verbose.log">[verbose log]</a> - 
        <a href="plots/{name}.pdf">[pdf]</a>
    </td>\n'''.format(image=image_file, name=image_file.split(".")[-2])
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path_to_files', type=str, required=True)
    parser.add_argument('-n', '--name', type=str, required=True)
    args = parser.parse_args()

    writeHTML(args.path_to_files.rstrip("/*"), args.name)

if __name__ == "__main__":
    main()

