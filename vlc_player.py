from vlc import Instance

class VLC:
    def __init__(self, tracklist=None, remote=False, password=None):
        args = ''
        if remote:
            passwd='vlcremote' if password is None else password
            args='--extraintf http --http-password {}'.format(passwd)
        self.Player = Instance(args)
        self.list_player = self.Player.media_list_player_new()
        if tracklist is not None:
            self.append_playlist(tracklist)

    def new_playlist(self, tracklist):
        self.list_player = self.Player.media_list_player_new()
        self.append_playlist(tracklist)

    def append_playlist(self, tracklist):
        self.media_list = self.Player.media_list_new()
        for track in tracklist:
            # location may be a URI or a list of URIs
            uri = track.location[0] if type(track.location) is list else track.location
            self.media_list.add_media(self.Player.media_new(uri))
        self.list_player.set_media_list(self.media_list)

    def is_playing(self):
        return self.list_player.is_playing()

    def play(self):
        # setting volume
        self.list_player.get_media_player().audio_set_volume(50)
        self.list_player.play()

    def next(self):
        self.list_player.next()
    def pause(self):
        self.list_player.pause()
    def previous(self):
        self.list_player.previous()
    def stop(self):
        self.list_player.stop()

    def exit(self):
        self.Player.release()
