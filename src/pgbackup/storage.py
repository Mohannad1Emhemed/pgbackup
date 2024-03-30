def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()

def s3(client, infile, bucket, name):
    client.upload_fileobj(infile, bucket, name)

#with open(infile_path, 'rb') as infile:
    #storage.s3(client, infile, 'python-db-backups-posgresql', infile.name)