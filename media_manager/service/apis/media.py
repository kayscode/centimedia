import requests


class SourceMediaFileService:

    @classmethod
    def get_media_files(cls, endpoints: list):
        media_files = []
        if len(endpoints) == 1:
            media_files.append(requests.get(endpoints[0]))
        elif len(endpoints) > 1 :
            for endpoint in endpoints:
                media_files.append(requests.get(endpoint))

        return media_files
